from Robot import Robot

class nodoDoble:
    def __init__(self, tipo = None, capacidad_combate=None, nombre_r = None, siguiente= None, anterior = None):
        self.tipo = tipo
        self.capacidad_combate = capacidad_combate
        self.nombre_r = nombre_r
        self.siguiente = siguiente
        self.anterior = anterior

class Lista_Robots:
    def __init__(self):
        self.raiz = nodoDoble()
        self.ultimo = self.raiz

    def insertarRobot(self,nuevonodo):
        if self.raiz.tipo is None:
            self.raiz = nuevonodo
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevonodo
            nuevonodo.anterior = self.raiz
            self.ultimo = nuevonodo
        else:
            self.ultimo.siguiente = nuevonodo
            nuevonodo.anterior = self.ultimo
            self.ultimo=nuevonodo

    def recorrerRobot(self):
        nodoaux = self.raiz
        cadena = ''
        while True:
            if nodoaux.tipo is not None:
                cadena += "Tipo: " + nodoaux.tipo + " Capacidad: "+ nodoaux.capacidad_combate + "Nombre: " + nodoaux.nombre_r
                if nodoaux.siguiente is not None:
                    cadena +="\n"
                    nodoaux = nodoaux.siguiente
                else: 
                    break
            else:
                break
        print(cadena)