class Zoologico:

  def __init__(self, nombre="", ubicacion=""):
    self._nombre = nombre
    self._ubicacion = ubicacion
    self._zonas = []

  def getNombre(self):
    return self._nombre

  def setNombre(self, nuevoNombre):
    self._nombre = nuevoNombre

  def getUbicacion(self):
    return self._ubicacion

  def setUbicacion(self, nuevaUbicacion):
    self._ubicacion = nuevaUbicacion

  def getZona(self):
    return self._zonas

  def setZona(self, nuevasZonas):
    self._zonas = nuevasZonas

  def cantidadTotalAnimales(self):
    contador = 0
    for zona in self._zonas:
      contador += zona.cantidadAnimales()
    return contador

  def agregarZonas(self, zona):
    self._zonas.append(zona)