import json
import os
import os.path
import logging
import sys, traceback
from datetime import datetime, date, time
from QueueModel import QueueModel
from PropertyUtil import PropertyUtil
from MailUtil import MailUtil
from UniqueIdUtil import UniqueIdUtil
from email.mime.text import MIMEText
class Processor:
	queueModel = QueueModel()
	def __init__(self,message):
		self.data = json.loads(message)
		self.queueModel.setFileName(self.data['fileName'])
		self.queueModel.setPath(self.data['path'])
		self.queueModel.setTimeStamp(self.data['timeStamp'])
		self.queueModel.setEmail(self.data['email'])
		self.queueModel.setOutputDir(self.data['outputDir'])
		uniqueIdUtil = UniqueIdUtil(self.data['fileName'])
		self.outputFile = uniqueIdUtil.getOutputUniqueID()

	def process(self):
		try:
			logging.debug('in process')
			originalFilename = self.getOriginalFileName(self.queueModel.getFileName(), self.queueModel.getPath())
			self.logNumberOfLines(originalFilename, self.queueModel.getFileName(), self.queueModel.getPath())
			self.generateMetadataFile()
			outputFile = self.queueModel.getOutputDir() + '/' + PropertyUtil.getAttribute('output.file.pre') + self.queueModel.getFileName()
			outputFile2 = self.queueModel.getOutputDir() + '/' + self.outputFile
			outputFile3 = self.queueModel.getOutputDir() + '/' + self.outputFile + '.png'
			fullCmd = PropertyUtil.getAttribute('fullCmd') + ' ' + self.queueModel.getPath() + '/' + self.queueModel.getFileName() + \
			  ' ' + outputFile + ' ' + outputFile3
			logging.debug(fullCmd)
			os.system(fullCmd)
			os.system('mv '+ outputFile + ' ' + outputFile2)
			logging.debug('emailing ...')
                	mailContent = "The file (" \
                                + self.queueModel.getFileName() \
                                + ") you uploaded on " \
                                + self.queueModel.getTimeStamp() \
                                + " has been processed.\n" \
                                + "\nYou can view the result page at: " \
                                + self.queueModel.getAccessLink() \
                                + ". This link will expire two weeks from today." \
                                + "\r\n\r\n - SOCcer Team \r\n (Note: Please do not reply to this email. If you need assistance, please contact NCISOCcerWebAdmin@mail.nih.gov)"
                	msg = MIMEText(mailContent)
                	msg['Subject'] = 'Your request has been processed'
                	msg['From'] = 'SOCcer <do.not.reply@mail.nih.gov>'
                	msg['To'] = self.queueModel.getEmail() 

			MailUtil.composeMail(msg)
		except:
			logging.error('Unable to process the request...')
			logging.error(traceback.format_exc())

	def getOriginalFileName(self, fileName, path):
		jsonString = path + "/" + fileName + ".json"
		print jsonString
		with open(jsonString) as metaFile:
			metadata = json.load(metaFile)
		if metadata.get('fileName'):
			return metadata['fileName']
		else:
			return ''

	def logNumberOfLines(self, originalFileName, fileName, path):
		logfile = PropertyUtil.getAttribute('deploy.target.dir') + '/' +  PropertyUtil.getAttribute('log.fileName')
		if not os.path.exists(logfile):
			with open(logfile,"w") as logF:
				logF.write("Timestamp, Input file Name, Number of Lines")
		logLineContent = '\n' + str(datetime.now()) + '\t' + originalFileName + '\t' + str(self.getNumberOfLines(path+'/'+fileName))
		with open(logfile,"a") as logF:
			logF.write(logLineContent)			
		
	def getNumberOfLines(self, fileName):
		with open(fileName) as datafile:
			totalLine = sum(1 for _ in datafile)
		return totalLine

	def generateMetadataFile(self):
		metadataFileName = self.queueModel.getPath() + '/' + self.outputFile + '.json'
		with open(metadataFileName,"w") as metadataF:
			json.dump(self.data, metadataF)

