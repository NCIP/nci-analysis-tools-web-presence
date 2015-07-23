import ConfigParser

class PropertyUtil:
	cp = ConfigParser.SafeConfigParser()
	cp.optionxform=str
	cp.read(r"config.ini")
	properties = {}

	for section in cp.sections():
		for option in cp.options(section):
			properties[option]=cp.get(section,option)
	print properties
	@staticmethod
	def getAttribute(att):
		return PropertyUtil.properties[att]

