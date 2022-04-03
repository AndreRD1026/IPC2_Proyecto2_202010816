from Lista_UM import Lista_UM
from Lista_Robots import Lista_Robots
class Ciudad:
    def __init__(self, nombre, unidades):
        self.nombre = nombre
        self.unidades : Lista_UM() = unidades 
        #self.robots : Lista_Robots() = robots
        #self.filas = filas
        #self.coordenadaInicio = coordenadaInicio
        #self.coordenadaFinal = coordenadaFinal
        #self.matrizTerreno = Matriz()
        #self.coordenadasRuta = ListaDoble()
        #self.robot = 0
        self.siguiente = None
        self.procesado = False
    
    def getUnidades(self):
        return self.unidades
    
