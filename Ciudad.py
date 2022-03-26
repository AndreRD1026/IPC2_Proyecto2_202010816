class Ciudad:
    def __init__(self, nombre,filas):
        self.nombre = nombre
        self.filas = filas
        #self.coordenadaInicio = coordenadaInicio
        #self.coordenadaFinal = coordenadaFinal
        #self.matrizTerreno = Matriz()
        #self.coordenadasRuta = ListaDoble()
        #self.gasRuta = 0
        self.siguiente = None
        self.procesado = False