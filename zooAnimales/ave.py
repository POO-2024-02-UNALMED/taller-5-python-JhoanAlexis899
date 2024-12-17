from zooAnimales.animal import Animal


class Ave(Animal):
  _listado = []
  halcones = 0
  aguilas = 0

  def __init__(self, nombre="", edad=0, habitat="", genero="", colorPlumas=""):
    super().__init__(nombre, edad, habitat, genero)
    self._colorPlumas = colorPlumas
    Ave._listado.append(self)

  def getColorPlumas(self):
    return self._colorPlumas

  def setColorPlumas(self, nuevasPlumas):
    self._colorPlumas = nuevasPlumas

  def getListado(self):
    return Ave._listado

  @classmethod
  def cantidadAves(cls):
    contador = 0
    for ave in cls._listado:
      if (isinstance(ave, Ave)):
        contador += 1
    return contador

  def movimiento(self):
    return "volar"

  @classmethod
  def crearHalcon(cls, nombre, edad, genero):
    cls.halcones += 1
    Ave(nombre, edad, "montana", genero, "cafe glorioso")

  @classmethod
  def crearAguila(cls, nombre, edad, genero):
    cls.aguilas += 1
    Ave(nombre, edad, "montana", genero, "blanco y amarillo")
    