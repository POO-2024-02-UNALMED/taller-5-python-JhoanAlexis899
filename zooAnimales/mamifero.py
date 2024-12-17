from zooAnimales.animal import Animal

class Mamifero(Animal):
  _listado = []
  caballos = 0
  leones = 0
  def __init__(self, nombre="", edad=0, habitat="", genero="", pelaje=False, patas=0):
    super().__init__(nombre, edad, habitat, genero)
    self._pelaje = pelaje
    self._patas = patas
    Mamifero._listado.append(self)

  def isPelaje(self):
    return self._pelaje

  def setPelaje(self, nuevoPelaje):
    self._pelaje = nuevoPelaje

  def getPatas(self):
    return self._patas

  def setPatas(self, nuevasPatas):
    self._patas = nuevasPatas

  def getListado(self):
    return Mamifero._listado

  @classmethod
  def cantidadMamiferos(cls):
    contador = 0
    for mamifero in cls._listado:
      if (isinstance(mamifero, Mamifero)):
        contador += 1
    return contador

  @classmethod
  def crearCaballo(cls, nombre, edad, genero):
    cls.caballos += 1
    Mamifero(nombre, edad, "pradera", genero, True, 4)

  @classmethod
  def crearLeon(cls, nombre, edad, genero):
    cls.leones += 1
    Mamifero(nombre, edad, "selva", genero, True, 4)
    