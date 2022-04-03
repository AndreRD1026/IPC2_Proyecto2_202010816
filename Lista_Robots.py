from Robot import Robot
class Lista_Robots:
    def __init__(self):
        self.inicio = None
        self.largoRobot = 0

    def agregarRobot(self, tipo,capcidad_combate,nombre_r):
        nuevoRobot = Robot(tipo,capcidad_combate,nombre_r)
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
            if tmp.getCapacidad_Combate() == 0:
                print("Nombre: " , tmp.getNombre_R(), " Tipo: " , tmp.getTipo() )
            else:
                 print("Nombre: " , tmp.getNombre_R(), " Tipo: " , tmp.getTipo(), " Capacidad: " , str(tmp.getCapacidad_Combate()))
            tmp = tmp.siguiente


    def obtenerTipoRescue(self):
        tmp = self.inicio
        robotsr = 0
        while tmp is not None:
            if tmp.getTipo() == 'ChapinRescue':
                print("Nombre: ", tmp.getNombre_R())
                robotsr += 1    
            tmp = tmp.siguiente
        return robotsr

    def obtenerTipoFighter(self):
        tmp = self.inicio
        robotsf = 0
        while tmp is not None:
            if tmp.getTipo() == 'ChapinFighter':
                print("Nombre: ", tmp.getNombre_R(), " Capacidad: ", tmp.getCapacidad_Combate())
                robotsf += 1    
            tmp = tmp.siguiente
        return robotsf



    def buscarRobot(self, nombre_r):
        tmp = self.inicio
        while tmp is not None:
            if tmp.nombre_r == nombre_r:
                return tmp 
            tmp = tmp.siguiente
        return False

    def getTipo(self, tipo):
        tmp = self.inicio
        while tmp is not None:
            if tmp.getTipo() == tipo:
                return tmp 
            tmp = tmp.siguiente
        return False

    def buscarRobotmision(self, nombre_r, tipo):
        tmp= self.inicio
        while tmp is not None:
            if tmp.getNombre_R() == nombre_r and tmp.getTipo() == tipo:
                return tmp
            tmp = tmp.siguiente
        return False