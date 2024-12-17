from zooAnimales.animal import Animal


class Pez(Animal):
  _listado = []
  salmones = 0
  bacalaos = 0

  def __init__(self, nombre="", edad=0, habitat="", genero="", colorEscamas="",cantidadAletas=0):
    super().__init__(nombre, edad, habitat, genero)
    self._colorEscamas = colorEscamas
    self._cantidadAletas = cantidadAletas
    Pez._listado.append(self)

  def getColorEscamas(self):
    return self._colorEscamas

  def setColorEscamas(self, nuevasEscamas):
    self._colorEscamas = nuevasEscamas

  def getCantidadAletas(self):
    return self._cantidadAletas

  def setCantidadAletas(self, nuevasAletas):
    self._cantidadAletas = nuevasAletas

  def getListado(self):
    return Pez._listado

  @classmethod
  def cantidadPeces(cls):
    contador = 0
    for pez in cls._listado:
      if (isinstance(pez, Pez)):
        contador += 1
    return contador

  def movimiento(self):
    return "nadar"

  @classmethod
  def crearSalmon(cls, nombre, edad, genero):
    cls.salmones += 1
    Pez(nombre, edad, "oceano", genero, "rojo", 6)

  @classmethod
  def crearBacalao(cls, nombre, edad, genero):
    cls.bacalaos += 1
    Pez(nombre, edad, "oceano", genero, "gris", 6)