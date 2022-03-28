class Unidad_Militar:
    def __init__(self, posx, posy, capacidad):
        self.posx = posx
        self.posy = posy
        self.capacidad = capacidad
        self.siguiente = None

    def getPosX(self):
        return self.posx
    def setPosX(self, posx):
        self.posx = posx
    def getPosY(self):
        return self.posy
    def setPosY(self, posy):
        self.posy = posy



