class Cliente():
	""" Conjunto de herramientas utilizadas en la granja de animales """
	def __init__(self, nombre, apellido, telefono, cantidadAnimales, pesos, metodoPago, referencia):

		self.nombre = nombre 
		self.apellido = apellido 
		self.telefono = telefono
		self.cantidadAnimales = cantidadAnimales
		self.pesos = pesos
		self.metodoPago = metodoPago
		self.referencia = referencia

	def getNombre(self): return self.nombre 

	def setNombre(self, nombre):
		self.nombre = nombre 

	def getApellido(self):
		return self.Apellido

	def setApellido(self, apellido):
		self.apellido = apellido 

	def getTelefono(self):
		return self.telefono

	def setTelefono(self, telefono):
		self.telefono = telefono;
