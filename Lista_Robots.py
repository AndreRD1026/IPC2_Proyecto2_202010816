from Robot import Robot
class Lista_Robots:
    def __init__(self):
        self.inicio = None
        self.largoRobot = 0

    def agregarRobot(self, tipo,capacidad_combate,nombre_r):
        nuevoRobot = Robot(tipo,capacidad_combate,nombre_r)
        self.largoRobot +=1
        if self.inicio == None:
            self.inicio = nuevoRobot
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevoRobot
        
    def mostrarRobot(self):
        tmp = self.inicio
        while tmp is not None:
            #time.sleep(0.5)
            print("Nombre: " + tmp.getNombre(), "Tipo: " + tmp.getTipo(), "Capacidad: " + tmp.getCapacidad_Combate() )
            tmp = tmp.siguiente

    def buscarRobot(self, nombre_r):
        tmp = self.inicio
        while tmp is not None:
            if tmp.nombre_r == nombre_r:
                return tmp 
            tmp = tmp.siguiente
        return False