from Robot import Robot
class Lista_Robots:
    def __init__(self):
        self.inicio = None
        self.largoRobot = 0
    #Agregado robots
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


    def obtenerCapacidad(self,nombre_r):
        tmp = self.inicio
        robotsf = 0
        while tmp is not None:
            if tmp.nombre_r == nombre_r:
                #print("Capacidad: ", tmp.getCapacidad_Combate())
                tmp.getCapacidad_Combate()
                robotsf = tmp.getCapacidad_Combate() 
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

    def actualizarRobots(self, nombre_r):
        tmp = self.inicio
        while tmp is not None:
            if tmp.nombre_r == nombre_r:
                self.inicio = tmp.siguiente
                tmp.siguiente = None
                print('Robot ',nombre_r, ' se ha actualizado')
                break
            elif tmp.siguiente is not None:
                if tmp.siguiente.nombre_r == nombre_r:
                    Nodo_a_borrar = tmp.siguiente
                    tmp.siguiente = Nodo_a_borrar.siguiente
                    Nodo_a_borrar.siguiente = None
                    print('Robot ', nombre_r,' se ha actualizado')
                    break
            tmp = tmp.siguiente