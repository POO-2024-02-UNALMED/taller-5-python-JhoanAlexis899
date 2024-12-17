class Animal:
  _totalAnimales = 0

  def __init__(self, nombre="", edad=0, habitat="", genero=""):
    self._nombre = nombre
    self._edad = edad
    self._habitat = habitat
    self._genero = genero
    self._zona = None
    Animal._totalAnimales += 1

  def getNombre(self):
    return self._nombre

  def setNombre(self, nuevoNombre):
    self._nombre = nuevoNombre

  def getEdad(self):
    return self._edad

  def setEdad(self, nuevaEdad):
    self._edad = nuevaEdad

  def getHabitat(self):
    return self._habitat

  def setHabitat(self, nuevoHabitat):
    self._habitat = nuevoHabitat

  def getGenero(self):
    return self._genero

  def setGenero(self, nuevoGenero):
    self._genero = nuevoGenero

  def movimiento(self):
    return "desplazarse"

  @classmethod
  def totalPorTipo(cls):
    from zooAnimales.anfibio import Anfibio
    from zooAnimales.ave import Ave
    from zooAnimales.mamifero import Mamifero
    from zooAnimales.pez import Pez
    from zooAnimales.reptil import Reptil
    return f"Mamiferos : {str(Mamifero.cantidadMamiferos())}\nAves : {str(Ave.cantidadAves())}\nReptiles : {str(Reptil.cantidadReptiles())}\nPeces : {str(Pez.cantidadPeces())}\nAnfibios : {str(Anfibio.cantidadAnfibios())}"

  def toString(self):
    if self._zona == None:
      return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
    return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona.getNombre()}, en el {self._zona.getZoo()}"