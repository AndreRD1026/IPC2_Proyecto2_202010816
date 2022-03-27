from Ciudad import Ciudad
#from coordenada import Coordenada
import time
class ListaSimple:
    def __init__(self):
        self.inicio = None
        self.largo = 0

    def agregar(self, nombre):
        nuevaCiudad = Ciudad(nombre)
        self.largo +=1
        if self.inicio == None:
            self.inicio = nuevaCiudad
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevaCiudad
    def mostrarElementos(self):
        tmp = self.inicio
        while tmp is not None:
            time.sleep(0.5)
            print("Ciudad: " + tmp.nombre)
            #print("Filas: " + tmp.filas)          
            print("")
            tmp = tmp.siguiente

    def buscarCiudad(self,nombre):
        tmp = self.inicio
        while tmp is not None:
            if tmp.nombre == nombre:
                return tmp 
            tmp = tmp.siguiente
        return None
    def getCiudad(self,posicion):
        contador = 1
        tmp = self.inicio
        while tmp is not None:
            if contador is posicion:
                return tmp
            tmp = tmp.siguiente
            contador +=1
        return None

        
    
            
