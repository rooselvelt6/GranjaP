import datetime

class Animal:
  """ Clase Animal para el control de la granja de pollos de engorde """
  def __init__(self, lote, tipoProduccion, raza, cantidad, precioUnitario):
    """ Constructor de pollos de engorde """
    self.lote = lote # Nª Lote

    self.tipoProduccion = tipoProduccion # Tipo de producción (Carne, Huevos)
    
    self.raza = raza #  Raza del animal comprado
    
    self.cantidad = cantidad # Cantidad de animales comprados para este lote
    
    self.precioUnitario = precioUnitario # Precio de los animales cuando fueron adquiridos

    self.fechaInicio = datetime.date.fromisoformat('2022-02-02')

    self.periodo = 45 # Cantidad de dias que dura un periodo de animales en el proceso de crianza

    self.muertes = {"ahogamiento":0, 
                    "infarto":0, 
                    "aplastamiento":0, 
                    "liquidos":0, 
                    "gases":0} # Muertes 

    self.congelados = [] # Lista de pollos congelados 

    self.sacrificados = [] # Lista de pollos sacrificados 

    self.vendidos = [] # Lista de pollos vendidos incluyen el consumo personal

  def getLote(self):
    """ Obtener el nùmero del lote de animales """
    return self.lote

  def setLote(self, lote):
    """ Cambiar el nùmero del lote de animales """
    self.lote = lote
    print("Nº Lote ha sido actualizado con èxito", self.lote)

  def getTipoProduccion(self):
    """ Obtener el tipo de producción de animales """
    return self.tipoProduccion

  def setTipoProduccion(self, tipoProduccion):
    """ Cambiar el tipo de producciòn de los animales """
    self.tipoProduccion = tipoProduccion

  def getRaza(self):
    """ Obtener la raza de los animales """ 
    return self.raza

  def setRaza(self, raza):
    """ Cambiar la raza de los animales """
    self.raza = raza

  def getCantidad(self, cantidad):
    """ Obtener la cantidad de animales comprados """
    self.cantidad = cantidad

  def setCantidad(self, cantidad):
    """ Actualizar la cantidad de animales adquiridos 
    Permite realizar la reposiciòn de pollos cuando sea necesario
    """
    self.cantidad = cantidad

  def getPrecioUnitario(self): 
    """ Obtener el precio unitario por animal """
    return self.precioUnitario;

  def setPrecioUnitario(self, precioUnitario):
    """ Cambiar el precio unitario por animal """
    self.precioUnitario = precioUnitario  

  def getFechaInicial(self):
    """ Obtener la fecha de inicio del animal """
    return self.fechaInicio

  def calcularFechaFinal(self):
    """ Calcular la fecha final para finalizar un ciclo de crianza de pollos """
    fechaFinal = self.fechaInicio + datetime.timedelta(days=45)
    return fechaFinal;

  def calcularCiclo(self):
    """ Cantidad de días que dura el ciclo completo del pollo """
    return (self.calcularFechaFinal() - self.fechaInicio).days

  def calcularGastoBruto(self):
    return self.cantidad * self.precioUnitario

  def calcularAnimalesMuertos(self):
    return sum(self.muertes.values())

  def cantidadTotalAnimales(self):
    return (len(self.congelados) + len(self.sacrificados) + len(self.vendidos))
  
  def sacrificar(self):
    cantidad = int(input("Cantidad de animales a sacrificar:"))
    for x in range(cantidad):
      peso1 = float(input("Ingrese el peso del animal vivo:"))
      self.sacrificados.append((peso1))

  def mostrarPollosSacrificados(self):
    return self.sacrificados

  def calcularTotalKgVendidos(self):
    return sum(self.vendidos)
  
  def calcularTotalKgCongelados(self):
    return sum(self.congelados)

  def calcularTotalKgSacrificados(self):
    return sum(self.sacrificados)

  def obtenerInforme(self):
    print("*******************************")
    print("REPORTE DE ANIMALES")
    print("*******************************")
    print("Nº LOTE: ", self.lote)
    print("Tipo de producciòn", self.tipoProduccion)
    print("Raza:", self.raza)
    print("Cantidad obtenida:", self.cantidad)
    print("Precio Unitario:", self.precioUnitario,"USD")
    print("Fecha de inicio de periodo: ", self.getFechaInicial())
    print("Fecha final del periodo:", self.calcularFechaFinal())
    print("Duración éstandar:", self.calcularCiclo())
    print("Inversión bruta:", self.calcularGastoBruto(),"USD")
    print("Cantidad de animales muertos:", self.calcularAnimalesMuertos())
    print("Perdidas por animales muertos:", self.calcularAnimalesMuertos()* self.precioUnitario, "USD")
    print("Total de animales:", self.cantidadTotalAnimales())
    
    print("Sacrificios realizados:", self.mostrarPollosSacrificados())
    print("Cantidad de Kg sacrificados: ", self.calcularTotalKgSacrificados())
    print("Cantidad de Kg congelados: ", self.calcularTotalKgCongelados())
    print("Cantidad de Kg vendidos: ", self.calcularTotalKgVendidos())
