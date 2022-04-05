from Lista_UM import Lista_UM
from Nodo_Encabezado import Nodo_Encabezado
from Lista_Encabezado import Lista_Encabezado
import os
import webbrowser

# -----------------------------Codigo de MATRIZ DISPERSA ----------------

class Nodo_Interno(): # Nodos ortogonales
    def __init__(self, x, y, caracter):# 'caracter' puede ser cualquier valor
        self.caracter = caracter
        self.coordenadaX = x  # fila
        self.coordenadaY = y  # columna
        self.arriba = None
        self.abajo = None
        self.derecha = None  # self.siguiente
        self.izquierda = None  # self.anterior


class MatrizDispersa():
    def __init__(self, capa, nombre, unidades):
        self.capa = capa
        self.nombre = nombre
        self.unidades : Lista_UM() = unidades 
        self.filas = Lista_Encabezado('fila')
        self.columnas = Lista_Encabezado('columna')
        self.civil = 0
        self.recursos = 0
        self.siguiente = None

    def getUnidades(self):
        return self.unidades
    
    def getUnidadesCiviles(self):
        return self.civil

    def getRecursos(self):
        return self.recursos


    def mostrarUC(self):
        tmp = self.filas.primero
        while tmp is not None:
            nodoCivil = tmp.acceso
            while nodoCivil is not None:
                if nodoCivil.caracter == 'C':
                    print("X: " + str(nodoCivil.coordenadaX), "Y: " + str(nodoCivil.coordenadaY))
                nodoCivil = nodoCivil.derecha
            tmp = tmp.siguiente

    def buscarUC(self, coordenadaX, coordenadaY):
        tmp = self.filas.primero
        while tmp is not None:
            nodoCivil = tmp.acceso
            while nodoCivil is not None:
                if str(nodoCivil.coordenadaX) == str(coordenadaX) and str(nodoCivil.coordenadaY) == str(coordenadaY) :
                    #print("X: " + str(nodoCivil.coordenadaX), "Y: " + str(nodoCivil.coordenadaY))
                    return nodoCivil
                nodoCivil = nodoCivil.derecha
            tmp = tmp.siguiente
        return False

    def mostrarEntrada(self):
        tmp = self.filas.primero
        while tmp is not None:
            nodoEntrada = tmp.acceso
            while nodoEntrada is not None:
                if nodoEntrada.caracter == 'E':
                    print("Pos X: " + str(nodoEntrada.coordenadaX), " Pos Y: " + str(nodoEntrada.coordenadaY))
                nodoEntrada = nodoEntrada.derecha
            tmp = tmp.siguiente
        return False

    def buscarEntrada(self):
        tmp = self.filas.primero
        while tmp is not None:
            nodoEntrada = tmp.acceso
            while nodoEntrada is not None:
                if nodoEntrada.caracter == 'E':
                    print("Pos X: " + str(nodoEntrada.coordenadaX), " Pos Y: " + str(nodoEntrada.coordenadaY))
                    return nodoEntrada
                nodoEntrada = nodoEntrada.derecha
                
            tmp = tmp.siguiente
        return False
    
    def mostrarRecurso(self):
        tmp = self.filas.primero
        while tmp is not None:
            nodoRecurso = tmp.acceso
            while nodoRecurso is not None:
                if nodoRecurso.caracter == 'R':
                    print("Posición X: " + str(nodoRecurso.coordenadaX), " Poisción Y: " + str(nodoRecurso.coordenadaY))
                nodoRecurso = nodoRecurso.derecha
            tmp = tmp.siguiente


    
    # (filas = x, columnas = y)
    def insert(self, pos_x, pos_y, caracter):
        nuevo = Nodo_Interno(pos_x, pos_y, caracter) # se crea nodo interno
        # --- lo prinero sera buscar si ya existen los encabezados en la matriz
        nodo_X = self.filas.getEncabezado(pos_x)
        nodo_Y = self.columnas.getEncabezado(pos_y)

        if nodo_X == None: # --- comprobamos que el encabezado fila pos_x exista
             # --- si nodo_X es nulo, quiere decir que no existe encabezado fila pos_x
            nodo_X = Nodo_Encabezado(pos_x)
            self.filas.insertar_nodoEncabezado(nodo_X)

        if nodo_Y == None: # --- comprobamos que el encabezado columna pos_y exista
            # --- si nodo_Y es nulo, quiere decir que no existe encabezado columna pos_y
            nodo_Y = Nodo_Encabezado(pos_y)
            self.columnas.insertar_nodoEncabezado(nodo_Y)

        # ----- INSERTAR NUEVO EN FILA
        if nodo_X.acceso == None: # -- comprobamos que el nodo_x no esta apuntando hacia ningun nodoInterno
            nodo_X.acceso = nuevo
        else: # -- si esta apuntando, validamos si la posicion de la columna del NUEVO nodoInterno es menor a la posicion de la columna del acceso 
            if nuevo.coordenadaY < nodo_X.acceso.coordenadaY: 
                nuevo.derecha = nodo_X.acceso              
                nodo_X.acceso.izquierda = nuevo
                nodo_X.acceso = nuevo
            else:
                #de no cumplirse debemos movernos de izquierda a derecha buscando donde posicionar el NUEVO nodoInterno
                tmp : Nodo_Interno = nodo_X.acceso 
                while tmp != None:                      
                    if nuevo.coordenadaY < tmp.coordenadaY:
                        nuevo.derecha = tmp
                        nuevo.izquierda = tmp.izquierda
                        tmp.izquierda.derecha = nuevo
                        tmp.izquierda = nuevo
                        break;
                    elif nuevo.coordenadaX == tmp.coordenadaX and nuevo.coordenadaY == tmp.coordenadaY: #validamos que no haya repetidas
                        break;
                    else:
                        if tmp.derecha == None:
                            tmp.derecha = nuevo
                            nuevo.izquierda = tmp
                            break;
                        else:
                            tmp = tmp.derecha 

        # ----- INSERTAR NUEVO EN COLUMNA
        if nodo_Y.acceso == None:  # -- comprobamos que el nodo_y no esta apuntando hacia ningun nodoCelda
            nodo_Y.acceso = nuevo
        else: # -- si esta apuntando, validamos si la posicion de la fila del NUEVO nodoCelda es menor a la posicion de la fila del acceso 
            if nuevo.coordenadaX < nodo_Y.acceso.coordenadaX:
                nuevo.abajo = nodo_Y.acceso
                nodo_Y.acceso.arriba = nuevo
                nodo_Y.acceso = nuevo
            else:
                # de no cumplirse, debemos movernos de arriba hacia abajo buscando donde posicionar el NUEVO
                tmp2 : Nodo_Interno = nodo_Y.acceso
                while tmp2 != None:
                    if nuevo.coordenadaX < tmp2.coordenadaX:
                        nuevo.abajo = tmp2
                        nuevo.arriba = tmp2.arriba
                        tmp2.arriba.abajo = nuevo
                        tmp2.arriba = nuevo
                        break;
                    elif nuevo.coordenadaX == tmp2.coordenadaX and nuevo.coordenadaY == tmp2.coordenadaY: #validamos que no haya repetidas
                        break;
                    else:
                        if tmp2.abajo == None:
                            tmp2.abajo = nuevo
                            nuevo.arriba = tmp2
                            break
                        else:
                            tmp2 = tmp2.abajo

        ##------ Fin de insercion


    def graficarNeatoR(self, nombre, ciudad):
        contenido = '''digraph G{
    node[shape=box, width=1, height=1, fontname="Arial", fillcolor="white", style=filled]
    edge[style = "invis" arrowhead="none" arrowtail="none"]
    node[label = "capa:''' + str(self.capa) +'''" fillcolor="darkolivegreen1" pos = "-1,1!"]raiz;'''
        contenido += '''label = "{}" \nfontname="Arial Black" labelloc=t \nfontsize="30pt" \n \n
                    \n'''.format(nombre + "\n")
        

        # --graficar nodos ENCABEZADO
        # --graficar nodos fila
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            contenido += '\n\tnode[label = "{}" fillcolor="white" pos="-1,-{}!" shape=box]x{};'.format(pivote.id, 
            posx, pivote.id)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            contenido += '\n\tx{}->x{}[dir=none color="white"];'.format(pivote.id, pivote.siguiente.id)
            contenido += '\n\tx{}->x{}[dir=none color="white"];'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        contenido += '\n\traiz->x{}[dir=none color="white"];'.format(self.filas.primero.id)

        # --graficar nodos columna
        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            contenido += '\n\tnode[label = "{}" fillcolor="white" pos = "{},1!" shape=box]y{};'.format(pivotey.id, 
            posy, pivotey.id)
            pivotey = pivotey.siguiente
            posy += 1
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            contenido += '\n\ty{}->y{}[dir=none color="white"];'.format(pivotey.id, pivotey.siguiente.id)
            contenido += '\n\ty{}->y{}[dir=none color="white"];'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        contenido += '\n\traiz->y{}[dir=none color="white"];'.format(self.columnas.primero.id)

        #ya con las cabeceras graficadas, lo siguiente es los nodos internos, o nodosCelda
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda : Nodo_Interno = pivote.acceso
            while pivote_celda != None:
                # --- buscamos posy
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.coordenadaY: break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                if pivote_celda.caracter == '*':
                    contenido += '\n\tnode[label="*" fillcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'E':
                    contenido += '\n\tnode[label=" " fillcolor="green" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'C' :
                    #ciudad.civil += 1
                    ciudad.civil += 1
                    contenido += '\n\tnode[label=" " fillcolor="blue" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'R':
                    ciudad.recursos += 1
                    contenido += '\n\tnode[label=" " fillcolor="gray" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif ciudad.getUnidades().buscarUnidad(pivote_celda.coordenadaX,pivote_celda.coordenadaY) != False:
                    contenido += '\n\tnode[label=" " fillcolor="red" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == '=':
                    contenido += '\n\tnode[label=" " fillcolor="yellow" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                else:
                    contenido += '\n\tnode[label=" " fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    ) 
                pivote_celda = pivote_celda.derecha
            
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.derecha != None:
                    contenido += '\n\ti{}_{}->i{}_{}[dir=none color="white"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=none color="white"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                pivote_celda = pivote_celda.derecha
        
            contenido += '\n\tx{}->i{}_{}[dir=none color="white"];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\tx{}->i{}_{}[dir=none color="white"];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1
        
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda : Nodo_Interno = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.abajo != None:
                    contenido += '\n\ti{}_{}->i{}_{}[dir=none color="white"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=none color="white"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY) 
                pivote_celda = pivote_celda.abajo
            contenido += '\n\ty{}->i{}_{}[dir=none color="white"];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\ty{}->i{}_{}[dir=none color="white"];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
        #contenido += '\n\t'
        #contenido += 'end[shape=Msquare];'       
        contenido += '\n}' 
        dot = "Grafico/" + "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as grafo:
            grafo.write(contenido)
        result = "matriz_{}.pdf".format(nombre)
        os.system("neato -Tpdf " + dot + " -o " + result)
        #webbrowser.open(result)


    def graficarNeatoR1(self, nombre, ciudad, nombrerobot):
        contenido = '''digraph G{
    node[shape=box, width=1, height=1, fontname="Arial", fillcolor="white", style=filled]
    edge[style = "invis" arrowhead="none" arrowtail="none"]
    node[label = "capa:''' + str(self.capa) +'''" fillcolor="darkolivegreen1" pos = "-1,1!"]raiz;'''
        contenido += '''label = "{}" \nfontname="Arial Black" labelloc=t \nfontsize="30pt" \n \n
                    \n'''.format(nombre + "\n")
        contenido += '''label = "{}" \nfontname="Arial Black"  \nfontsize="30pt" \n \n
                    \n'''.format("Robot usado : ", nombrerobot)
        

        # --graficar nodos ENCABEZADO
        # --graficar nodos fila
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            contenido += '\n\tnode[label = "{}" fillcolor="white" pos="-1,-{}!" shape=box]x{};'.format(pivote.id, 
            posx, pivote.id)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            contenido += '\n\tx{}->x{}[dir=none color="white"];'.format(pivote.id, pivote.siguiente.id)
            contenido += '\n\tx{}->x{}[dir=none color="white"];'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        contenido += '\n\traiz->x{}[dir=none color="white"];'.format(self.filas.primero.id)

        # --graficar nodos columna
        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            contenido += '\n\tnode[label = "{}" fillcolor="white" pos = "{},1!" shape=box]y{};'.format(pivotey.id, 
            posy, pivotey.id)
            pivotey = pivotey.siguiente
            posy += 1
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            contenido += '\n\ty{}->y{}[dir=none color="white"];'.format(pivotey.id, pivotey.siguiente.id)
            contenido += '\n\ty{}->y{}[dir=none color="white"];'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        contenido += '\n\traiz->y{}[dir=none color="white"];'.format(self.columnas.primero.id)

        #ya con las cabeceras graficadas, lo siguiente es los nodos internos, o nodosCelda
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda : Nodo_Interno = pivote.acceso
            while pivote_celda != None:
                # --- buscamos posy
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.coordenadaY: break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                if pivote_celda.caracter == '*':
                    contenido += '\n\tnode[label="*" fillcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'E':
                    contenido += '\n\tnode[label=" " fillcolor="green" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'C' :
                    #ciudad.civil += 1
                    ciudad.civil += 1
                    contenido += '\n\tnode[label=" " fillcolor="blue" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'R':
                    ciudad.recursos += 1
                    contenido += '\n\tnode[label=" " fillcolor="gray" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif ciudad.getUnidades().buscarUnidad(pivote_celda.coordenadaX,pivote_celda.coordenadaY) != False:
                    contenido += '\n\tnode[label=" " fillcolor="red" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == '=':
                    contenido += '\n\tnode[label=" " fillcolor="yellow" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == '$':
                    contenido += '\n\tnode[label=" " fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                else:
                    contenido += '\n\tnode[label=" " fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    ) 
                pivote_celda = pivote_celda.derecha
            
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.derecha != None:
                    contenido += '\n\ti{}_{}->i{}_{}[dir=none color="white"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=none color="white"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                pivote_celda = pivote_celda.derecha
        
            contenido += '\n\tx{}->i{}_{}[dir=none color="white"];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\tx{}->i{}_{}[dir=none color="white"];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1
        
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda : Nodo_Interno = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.abajo != None:
                    contenido += '\n\ti{}_{}->i{}_{}[dir=none color="white"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=none color="white"];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY) 
                pivote_celda = pivote_celda.abajo
            contenido += '\n\ty{}->i{}_{}[dir=none color="white"];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\ty{}->i{}_{}[dir=none color="white"];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
        #contenido += '\n\t'
        #contenido += 'end[shape=Msquare];'       
        contenido += '\n}' 
        dot = "Grafico/" + "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as grafo:
            grafo.write(contenido)
        result = "matriz_{}_mision.pdf".format(nombre)
        os.system("neato -Tpdf " + dot + " -o " + result)
        #webbrowser.open(result)
