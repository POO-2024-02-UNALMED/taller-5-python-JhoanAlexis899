from zooAnimales.animal import Animal


class Reptil(Animal):
  _listado = []
  iguanas = 0
  serpientes = 0

  def __init__(self, nombre="", edad=0, habitat="", genero="", colorEscamas="", largoCola=0):
    super().__init__(nombre, edad, habitat, genero)
    self._colorEscamas = colorEscamas
    self._largoCola = largoCola
    Reptil._listado.append(self)

  def getColorEscamas(self):
    return self._colorEscamas

  def setColorEscamas(self, nuevasEscamas):
    self._colorEscamas = nuevasEscamas

  def getLargoCola(self):
    return self._largoCola

  def setLargoCola(self, nuevoLargo):
    self._largoCola = nuevoLargo

  def getListado(self):
    return Reptil._listado

  @classmethod
  def cantidadReptiles(cls):
    contador = 0
    for reptil in cls._listado:
      if (isinstance(reptil, Reptil)):
        contador += 1
    return contador

  def movimiento(self):
    return "reptar"

  @classmethod
  def crearIguana(cls, nombre, edad, genero):
    cls.iguanas += 1
    Reptil(nombre, edad, "humedal", genero, "verde", 3)

  @classmethod
  def crearSerpiente(cls, nombre, edad, genero):
    cls.serpientes += 1
    Reptil(nombre, edad, "jungla", genero, "blanco", 3)