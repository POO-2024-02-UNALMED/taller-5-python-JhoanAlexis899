from zooAnimales.animal import Animal


class Anfibio(Animal):
  _listado = []
  ranas = 0
  salamandras = 0

  def __init__(self, nombre="", edad=0, habitat="", genero="", colorPiel="", venenoso=False):
    super().__init__(nombre, edad, habitat, genero)
    self._colorPiel = colorPiel
    self._venenoso = venenoso
    Anfibio._listado.append(self)

  def isVenenoso(self):
    return self._venenoso

  def setVenenoso(self, nuevoVenenoso):
    self._venenoso = nuevoVenenoso

  def getColorPiel(self):
    return self._colorPiel

  def setColorPiel(self, nuevoColor):
    self._colorPiel = nuevoColor

  def getListado(self):
    return Anfibio._listado

  @classmethod
  def cantidadAnfibios(cls):
    contador = 0
    for anfibio in cls._listado:
      if (isinstance(anfibio, Anfibio)):
        contador += 1
    return contador

  def movimiento(self):
    return "saltar"

  @classmethod
  def crearRana(cls, nombre, edad, genero):
    cls.ranas += 1
    Anfibio(nombre, edad, "selva", genero, "rojo", True)

  @classmethod
  def crearSalamandra(cls, nombre, edad, genero):
    cls.salamandras += 1
    Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)