class Robot:
    def __init__(self, tipo,capacidad_combate, nombre_r):
        self.tipo = tipo
        self.capacidad_combate = capacidad_combate
        self.nombre_r = nombre_r
        self.siguiente = None

    def getTipo(self):
        return self.tipo
    def setTipo(self, tipo):
        self.tipo = tipo
    def getCapacidad_Combate(self):
        return self.capacidad_combate
    def setCapacidad_Combate(self, capacidad_combate):
        self.capacidad_combate = capacidad_combate
    def getNombre_R(self):
        return self.nombre_r
    def setNombre_R(self, nombre_r):
        self.nombre_r = nombre_r