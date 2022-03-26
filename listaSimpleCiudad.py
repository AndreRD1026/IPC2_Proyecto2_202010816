from Ciudad import Ciudad
#from coordenada import Coordenada
import time
class ListaSimple:
    def __init__(self):
        self.inicio = None
        self.largo = 0

    def agregar(self, nombre,filas):
        nuevaCiudad = Ciudad(nombre,filas)
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
            print("Filas: " + tmp.filas)
            #print("Coordenada inicial: [" + str(tmp.coordenadaInicio.x) +", " + str(tmp.coordenadaInicio.y) + "]")
            #print("Coordenada final: [" + str(tmp.coordenadaFinal.x) +", " + str(tmp.coordenadaFinal.y) + "]")
            #print("Matriz del Terreno - Dimensión " , tmp.matrizTerreno.n, "X", tmp.matrizTerreno.m, ":")
            #fila = ""
            #maximoGas = 0
            #for i in range(1,tmp.matrizTerreno.n +1):
            #    for j in range(1,tmp.matrizTerreno.m+1):
            #        if tmp.matrizTerreno.getGasNodo(i,j) > maximoGas:
            #            maximoGas = tmp.matrizTerreno.getGasNodo(i,j)
            #if maximoGas <10:
            #    maximoGas = 1
            #elif maximoGas<100:
            #    maximoGas = 2
            #elif maximoGas <1000:
            #    maximoGas = 3

            #for i in range(1,tmp.matrizTerreno.n +1):
            #    fila = ""
            #    for j in range(1,tmp.matrizTerreno.m+1):
            #        espacios = maximoGas - len(str(tmp.matrizTerreno.getGasNodo(i,j)))
            #        spaces = ""
            #        for k in range (0, espacios):
            #            spaces += " "
            #        fila+= "| " + str(tmp.matrizTerreno.getGasNodo(i,j)) + " " + spaces
            #    fila +="|"
            #    print(fila)              
            print("")
            tmp = tmp.siguiente

    def buscarCiudad(self,nombre):
        tmp = self.inicio
        while tmp is not None:
            if tmp.nombre == nombre:
                return tmp 
            tmp = tmp.siguiente
        return None
    def getTerreno(self,posicion):
        contador = 1
        tmp = self.inicio
        while tmp is not None:
            if contador is posicion:
                return tmp
            tmp = tmp.siguiente
            contador +=1
        return None

        
    
            
