from Lista_UM import Lista_UM
from Lista_Robots import Lista_Robots
class Ciudad:
    def __init__(self, nombre, unidades):
        self.nombre = nombre
        self.unidades : Lista_UM() = unidades 
        self.siguiente = None
        self.procesado = False
    
    def getUnidades(self):
        return self.unidades
    
