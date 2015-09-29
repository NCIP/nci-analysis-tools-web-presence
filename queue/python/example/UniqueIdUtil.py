import uuid
class UniqueIdUtil:
	fileext = ''
	filename = ''
	def __init__(self,filename):
		self.filename = filename
		pos = filename.rfind('.')
		if pos > 0:
			self.fileext='.' + filename[pos+1:len(filename)]
			self.filename=filename[0:pos]
	def getInputUniqueID(self):
		return self.filename+'_i_' + str(uuid.uuid4())  + self.fileext;
	def getOutputUniqueID(self):
		return self.filename+'_o_' + str(uuid.uuid4())  + self.fileext;
