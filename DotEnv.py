import configparser as config

class DotEnv:

	''' 
	' Author: Mina <mina.farag@icloud.com>
	'''


	''' 
	' Constructor
	'''
	def __init__(self,name='.env'):
		self._config = config.ConfigParser()
		self._file = name
	
	'''
	' Alternative constructor
	'''
	@classmethod
	def custom_init(cls,name):
		cls._file = name
		return cls(name)

	'''
	' Properties
	' [ Read only ]
	'''
	@property
	def file(self):
		return self._file
	
	@property
	def config(self):
		return self._config

	'''
	' Behavior
	'''
	
	''' Create file '''
	def create_file(self):
		self._config['main'] = {'key_1':'value_1'}
		with open(self.file,'w') as ConfigFile:
			self.config.write(ConfigFile)

	''' Read Key from file '''
	def read(self,key:str,section='main'):
		self._config.read(self.file)
		return self.config[section].get(key)
