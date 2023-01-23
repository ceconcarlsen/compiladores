class Errors(object):
	_instance = None
	def __new__(self, textOutput=None):
		if (self._instance is None):
			self._instance = super().__new__(self)

		return self._instance

	def __init__(self):
		self.ERROR_VARIABLE_NO_EXIST = "ERROR: variavel-nao-declarada"
		self.ERROR_TYPE = "ERROR: tipo"
		self.ERROR_VARIABLE_EXIST = "ERROR: variavel-ja-declarada"
		self.ERROR_VARIABLE_NO_VALUE = "ERROR: variavel-sem-valor"

		self.errorList = []

		self.WARNING_VARIABLE_WITHOUT_USE = "WARNING: variavel-nao-utilizada"
		self.warningList = []


		self.ERROR_PROCEDURE_NO_EXIST = "ERROR: procedure-nao-declarada"
		self.ERROR_PROCEDURE_EXIST = "ERROR: procedure-ja-declarada"

		self.ERROR_READ_PARAMETERS = "ERROR: parametros-read-incoerentes"
		
		

	def addError(self, error):
		self.errorList.append(error)
		return True

	def addWarning(self, warning):
		self.warningList.append(warning)
		return True

	def clearErrors(self):
		self.errorList = []
		return True

	def clearWarnings(self):
		self.warningList = []
		return True

	def getErrorList(self):
		return self.errorList

	def getWarningList(self):
		return self.warningList

	def hasErrors(self):
		if(len(self.errorList) > 0):
			return True

		return False