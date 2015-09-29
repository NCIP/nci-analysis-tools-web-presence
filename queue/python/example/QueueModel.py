
class QueueModel:

	fileName = ""
	path = ""
	email = ""
	timeStamp = ""
	outputDir = ""
	accessLink = ""

	def __init_(self):
		fileName = ""
		path = ""
		email = ""
		timeStamp = ""
		outputDir = ""
		accessLink = ""

	def getFileName(self):
		return self.fileName
	def getPath(self):
		return self.path
	def getEmail(self):
		return self.email
	def getTimeStamp(self):
		return self.timeStamp
	def getOutputDir(self):
		return self.outputDir
	def getAccessLink(self):
		return self.accessLink
	def setFileName(self, fileName):
		self.fileName=fileName
	def setPath(self, path):
		self.path = path
	def setTimeStamp(self, timeStamp):
		self.timeStam = timeStamp
	def setEmail(self, email):
		self.email = email
	def setOutputDir(self, outputDir):
		self.outputDir = outputDir
	def setAccessLink(self, accessLink):
		self.accessLink = accessLink
