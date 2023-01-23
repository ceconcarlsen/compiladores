from abc import ABC

# Infraestrutura parqa definir as caracteristicas das classes abstratas

class Variable(ABC):
	def __init__(self, name, address):
		self.name = name
		self.addressAllocated = address

	def getname(self):
		return self.name

	def setname(self, name):
		self.name = name

	def getAddressAllocated(self):
		return self.addressAllocated

	def setAddressAllocated(self, address):
		self.addressAllocated = address

class Integer(Variable):
	def __init__(self, name, address, value):
		super().__init__(name, address)

		self.value = value

	def getvalue(self):
		return self.value

	def setvalue(self, value):
		self.value = value

class Boolean(Variable):
	def __init__(self, name, address, value):
		super().__init__(name, address)
		self.value = value

	def getvalue(self):
		return self.value

	def setvalue(self, value):
		self.value = value

class Float(Variable):
	def __init__(self, name, address, value):
		super().__init__(name, address)

		self.value = float(value)

	def getvalue(self):
		return self.value

	def setvalue(self, value):
		self.value = value