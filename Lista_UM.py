from UnidadMilitar import Unidad_Militar
class Lista_UM:
    def __init__(self):
        self.inicio = None
        self.largoUM = 0

    def agregarUnidad(self, posx,posy,capacidad):
        nuevaUnidad = Unidad_Militar(posx,posy,capacidad)
        self.largoUM +=1
        if self.inicio == None:
            self.inicio = nuevaUnidad
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevaUnidad
        
    def mostrarUnidad(self):
        tmp = self.inicio
        while tmp is not None:
            print("Posicion X: " + tmp.getPosX(), "Posicion Y: " + tmp.getPosY(), "Capacidad: " + tmp.getCapacidad() )
            tmp = tmp.siguiente

    def buscarUnidad(self, posx, posy):
        tmp = self.inicio
        while tmp is not None:
            if tmp.getPosX() == str(posx) and tmp.getPosY() == str(posy) :
                return tmp 
            tmp = tmp.siguiente
        return False

    def buscarUnidad1(self, posx, posy):
        tmp = self.inicio
        while tmp is not None:
            if tmp.getPosX() == str(posx) and tmp.getPosY() == str(posy) :
                tmp.getCapacidad()
                capacidadrobot = tmp.getCapacidad()
            tmp = tmp.siguiente
        return capacidadrobot