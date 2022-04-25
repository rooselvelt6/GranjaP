class Herramienta():
	""" Conjunto de herramientas utilizadas en la granja de animales """
	def __init__(self, nombre, cantidad, precioUnitario):

		self.nombre = nombre 
		self.cantidad = cantidad 
		self.precioUnitario = precioUnitario

	def getNombre(self): return self.nombre 

	def setNombre(self, nombre):
		self.nombre = nombre 

	def getCantidad(self):
		return self.cantidad

	def setCantidad(self, cantidad):
		self.cantidad = cantidad 

	def getPrecioUnitario(self):
		return self.precioUnitario

	def setPrecioUnitario(self, precioUnitario):
		self.precioUnitario = precioUnitario;