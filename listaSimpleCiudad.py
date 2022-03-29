from Ciudad import Ciudad
from UnidadMilitar import Unidad_Militar
from Robot import Robot
#from coordenada import Coordenada
import time
class ListaSimple:
    def __init__(self):
        self.inicio = None
        self.largo = 0

    def agregar(self, nombre, unidades):
        nuevaCiudad = Ciudad(nombre,unidades)
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
            print("-" + tmp.nombre)
            #tmp.getUnidades().mostrarUnidad()
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

    def agregarUnidad(self, posx,posy,capacidad):
        nuevaUnidad = Unidad_Militar(posx,posy,capacidad)
        self.largo +=1
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
            time.sleep(0.5)
            print("Posicion X: " + tmp.getPosX())
            print("Posicion Y: " + tmp.getPosY())
            print("Capacidad: " + tmp.getCapacidad())
            tmp = tmp.siguiente

    '''def agregarRobot(self, tipo,capacidad_combate,nombre_r):
        nuevoRobot = Robot(tipo,capacidad_combate,nombre_r)
        self.largo +=1
        if self.inicio == None:
            self.inicio = nuevoRobot
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevoRobot '''
        
    '''def mostrarRobot(self):
        tmp = self.inicio
        while tmp is not None:
            time.sleep(0.5)
            print("Tipo: " + tmp.tipo)
            print("Capacidad: " + tmp.capacidad_combate)
            print("Nombre: " + tmp.nombre_r)
            tmp = tmp.siguiente '''
    
            
