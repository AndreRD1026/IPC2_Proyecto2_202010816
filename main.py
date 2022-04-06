import xml.etree.ElementTree as ET
from listaSimpleCiudad import ListaSimple as listaciudad
from Lista_UM import Lista_UM
from Lista_Robots import Lista_Robots
import graphviz
import time
from MatrizDispersa import MatrizDispersa
import webbrowser

ciudades = listaciudad()
robots = Lista_Robots()


archivoEntrada = None
rutaEntrada = None


def cargarArchivo1():
    global archivoEntrada
    global rutaEntrada
    global ciudades 
    global robots
    global unidades
    
    print("---------- Cargar Archivo ----------")
    Filename = input('Ingrese la ruta del archivo: ')
    file = Filename

    if str(file).endswith('.xml'):
        try:
            archivoEntrada = ET.parse(file)
            rutaEntrada = archivoEntrada.getroot()
            rutarobot = archivoEntrada.getroot()

            print(" El archivo se cargó con éxito ")
            print("")

            print("Analizando archivo...")

            for elemento in rutaEntrada:
                for subelemento in elemento:
                    if subelemento.tag == 'ciudad':
                        unidades = Lista_UM()
                        for subelemento1 in subelemento:
                            if subelemento1.tag == 'nombre':
                                nombre = subelemento1.text
                                if ciudades.buscarCiudad(nombre) != False:
                                    ciudades.actualizarCiudad(nombre)
                                doc = open("Salida/" + subelemento1.text + ".txt", "w")
                                #doc = open(subelemento1.text + ".txt", "w")
                            if subelemento1.tag == 'fila':
                                doc.write(subelemento1.text + '\n')
                            if subelemento1.tag == 'unidadMilitar':
                                unidades.agregarUnidad(subelemento1.attrib['fila'], subelemento1.attrib['columna'], subelemento1.text)
                        #ciudades.agregar(nombre, unidades)
                        doc.close()
                        ciudades.agregarMatriz(0, nombre, unidades)    
                    if subelemento.tag == 'robot':
                        for subelemento1 in subelemento:
                            if subelemento1.tag == 'nombre':
                                nombre_r = subelemento1.text
                                if robots.buscarRobot(nombre_r) != False:
                                    robots.actualizarRobots(nombre_r)
                                if 'capacidad' in subelemento1.attrib:
                                    robots.agregarRobot(subelemento1.attrib['tipo'], int(subelemento1.attrib['capacidad']), subelemento1.text)
                                else:
                                    robots.agregarRobot(subelemento1.attrib['tipo'],int(0), subelemento1.text)
            print("")
            print("-----Ciudades encontradas -----")
            print("")
            ciudades.mostrarElementos()
            print("") 
            print("----Robots encontrados----") 
            robots.mostrarRobot()
            time.sleep(0.5)
        except:
            print("")
            print("¡¡ ERROR !!")
            print("Ha ocurrido un error en la carga del archivo")

    else:
        print("¡¡ ERROR !!")
        print("El archivo cargado no es compatible con un .xml")



def realizarmision():
    global ciudad
    global nombrerobot
    global nombrerobot1
    global capacidadpelea
    ciudad = buscarciudad()
    print("")
    print("----Misiones Disponibles----")
    print("1. Rescate")
    print("2. Extracción de recursos")
    print("")
    nombremision = input("Elija una misión: ")
    print("")
    if nombremision == '1':
        print("--Mision de Rescate--")
        print("")
        if ciudad.getUnidadesCiviles() > 0: 
            print("-----Robots Disponibles-----""\n")
            if robots.obtenerTipoRescue() == 0:
                print("¡¡ Ha ocurrido un error !!")
                print("No existen robots para esta misión")
            else:
                nombrerobot = input("\n""Escriba el nombre del robot - ")
                if robots.buscarRobotmision(nombrerobot, 'ChapinRescue') != False:
                    print("")
                    print("---Unidades Civiles disponibles---")
                    ciudad.mostrarUC()
                    recorrerciudad(ciudad)

                else:
                    print("El robot no ha sido encontrado")
        else:
            print("Lo sentimos, la ciudad no cuenta con unidades civiles para completar la misión")
            
    if nombremision == '2':
        print("---Misión de Extracción de Recursos---")
        print("")
        if ciudad.getRecursos() > 0:
            print("-----Robots Disponibles-----")
            if robots.obtenerTipoFighter() == 0:
                print("¡¡ Ha ocurrido un error !!")
                print("No existen robots para esta misión")
            else:
                nombrerobot1 = input("\n""Escriba el nombre del robot - ")
                if robots.buscarRobotmision(nombrerobot1, 'ChapinFighter') != False:
                    print("")
                    print("---Recursos disponibles---")
                    capacidadpelea = robots.obtenerCapacidad(nombrerobot1)
                    #print(nombrerobot1 ,"+", robots.obtenerCapacidad(nombrerobot1))
                    ciudad.mostrarRecurso()
                    recorrerciudadRecurso(ciudad)
                else:
                    print("El robot no ha sido encontrado")
                    
        else:
            print("Lo sentimos, la ciudad no cuenta con recursos para completar la misión")


def recorrerciudad(ciudad):
    global Civilfinal
    global coordenadax
    global coordenaday
    print("")
    coordenadax = input("Ingrese la fila: ")
    coordenaday = input("Ingrese la columna: ")
    print("Seleccionó: ", coordenadax, coordenaday)
    #ciudad.buscarUC(coordenadax, coordenaday)
    
    if ciudad.buscarUC(coordenadax, coordenaday) is False:
        print("No ingresó una coordenada correcta")
    else:
        
        print("Examinando el camino hacia la coordenada")
        ciudad.mostrarEntrada()
        Civilfinal = ciudad.buscarUC(coordenadax, coordenaday)
        #misionCivil()
        tmp = ciudad.filas.primero
        while tmp is not None:
            nodoEntrada = tmp.acceso
            while nodoEntrada is not None:
                if nodoEntrada.caracter == 'E':
                    if misionCivil(nodoEntrada) == True:
                        break
                    #print("Pos X: " + str(nodoEntrada.coordenadaX), " Pos Y: " + str(nodoEntrada.coordenadaY))
                    #return nodoEntrada
                nodoEntrada = nodoEntrada.derecha
                
            tmp = tmp.siguiente
        #return False

def recorrerciudadRecurso(ciudad):
    global RecursoFinal
    global coordenadax
    global coordenaday
    print("")
    coordenadax = input("Ingrese la fila: ")
    coordenaday = input("Ingrese la columna: ")
    print("Seleccionó: ", coordenadax, coordenaday)
    #ciudad.buscarUC(coordenadax, coordenaday)
    
    if ciudad.buscarRecurso(coordenadax, coordenaday) is False:
        print("No ingresó una coordenada correcta")
    else:
        
        print("Examinando el camino hacia la coordenada")
        ciudad.mostrarEntrada()
        RecursoFinal = ciudad.buscarRecurso(coordenadax, coordenaday)
        #misionCivil()
        tmp = ciudad.filas.primero
        while tmp is not None:
            nodoEntrada = tmp.acceso
            while nodoEntrada is not None:
                if nodoEntrada.caracter == 'E':
                    if misionRecurso(nodoEntrada) == True:
                        break
                    #print("Pos X: " + str(nodoEntrada.coordenadaX), " Pos Y: " + str(nodoEntrada.coordenadaY))
                    #return nodoEntrada
                nodoEntrada = nodoEntrada.derecha
                
            tmp = tmp.siguiente
        #return False




def misionCivil(entrada):
    ciudad.limpiar()
    print("Entra en el recorrido la entrada")  
    #ciudad.buscarEntrada()
    #entrada = ciudad.buscarEntrada()
    llega = False
    while llega is False:
        if entrada != None and entrada.arriba == Civilfinal:
            llega = True
            ciudad.graficarNeatoR1(ciudad.nombre, ciudad, nombrerobot, coordenadax, coordenaday)
            return True
            break     
        elif entrada != None and entrada.izquierda == Civilfinal:
            llega = True
            ciudad.graficarNeatoR1(ciudad.nombre, ciudad, nombrerobot, coordenadax, coordenaday)
            return True
            break
        elif entrada != None and entrada.derecha == Civilfinal:
            llega = True
            ciudad.graficarNeatoR1(ciudad.nombre, ciudad, nombrerobot, coordenadax, coordenaday)
            return True
            break
        elif entrada != None and entrada.abajo == Civilfinal:
            llega = True
            ciudad.graficarNeatoR1(ciudad.nombre, ciudad, nombrerobot, coordenadax, coordenaday)
            return True
            break


        #Arriba - izquierda
        elif entrada != None and entrada.coordenadaY <= Civilfinal.coordenadaY and entrada.coordenadaX <= Civilfinal.coordenadaX:
            if entrada.derecha != None and entrada.derecha.caracter == ' ':
                entrada.derecha.caracter = '='
                entrada = entrada.derecha
            elif entrada.abajo != None and entrada.abajo.caracter == ' ':
                entrada.abajo.caracter = '='
                entrada = entrada.abajo
            elif entrada.abajo != None and entrada.abajo.caracter == 'C':
                entrada.abajo.caracter = 'C'
                entrada = entrada.abajo
            elif entrada.arriba != None and entrada.arriba.caracter == 'C':
                entrada.arriba.caracter = 'C'
                entrada = entrada.arriba
            elif entrada.izquierda != None and entrada.izquierda.caracter == 'C':
                entrada.izquierda.caracter = 'C'
                entrada = entrada.izquierda
            elif entrada.derecha != None and entrada.derecha.caracter == 'C':
                entrada.derecha.caracter = 'C'
                entrada = entrada.derecha
            elif entrada.arriba != None and entrada.arriba.caracter == ' ':
                entrada.arriba.caracter = '='
                entrada = entrada.arriba            
            elif entrada.izquierda != None and entrada.izquierda.caracter == ' ':
                entrada.izquierda.caracter = '='
                entrada = entrada.izquierda
            #Regresos
            elif entrada.derecha != None  and entrada.derecha.caracter != ' ':
                entrada.caracter = '$'
                #entrada.izquierda.caracter = '$'
                entrada = entrada.izquierda
            elif entrada.izquierda != None  and entrada.izquierda.caracter != ' ':
                entrada.caracter = '$'
                #entrada.derecha.caracter = '$'
                entrada = entrada.derecha
            elif entrada.arriba != None  and entrada.arriba.caracter != ' ':
                entrada.caracter = '$'
                #entrada.abajo.caracter = '$'
                entrada = entrada.abajo
            elif entrada.abajo != None  and entrada.abajo.caracter != ' ':
                entrada.caracter = '$'
                #entrada.arriba.caracter = '$'
                entrada = entrada.arriba
            #Regresos no camino
            elif entrada.derecha != None  and entrada.derecha.caracter == '*':
                entrada.caracter = '$'
                #entrada.izquierda.caracter = '$'
                entrada = entrada.izquierda
            elif entrada.izquierda != None  and entrada.izquierda.caracter == '*':
                entrada.caracter = '$'
                #entrada.derecha.caracter = '$'
                entrada = entrada.derecha
            elif entrada.arriba != None  and entrada.arriba.caracter == '*':
                entrada.caracter = '$'
                #entrada.abajo.caracter = '$'
                entrada = entrada.abajo
            elif entrada.abajo != None  and entrada.abajo.caracter == '*':
                entrada.caracter = '$'
                #entrada.arriba.caracter = '$'
                entrada = entrada.arriba
            elif entrada.derecha != None  and entrada.derecha.caracter == 'R':
                entrada.caracter = '$'
                #entrada.izquierda.caracter = '$'
                entrada = entrada.izquierda
            elif entrada.izquierda != None  and entrada.izquierda.caracter == 'R':
                entrada.caracter = '$'
                #entrada.derecha.caracter = '$'
                entrada = entrada.derecha
            elif entrada.arriba != None  and entrada.arriba.caracter == 'R':
                entrada.caracter = '$'
                #entrada.abajo.caracter = '$'
                entrada = entrada.abajo
            elif entrada.abajo != None  and entrada.abajo.caracter == 'R':
                entrada.caracter = '$'
                #entrada.arriba.caracter = '$'
                entrada = entrada.arriba


        #Abajo - Derecha
        elif entrada != None and entrada.coordenadaY >= Civilfinal.coordenadaY and entrada.coordenadaX >= Civilfinal.coordenadaX:
            if entrada.izquierda != None and entrada.izquierda.caracter == ' ':
                entrada.izquierda.caracter = '='
                entrada = entrada.izquierda
            elif entrada.arriba != None and entrada.arriba.caracter == ' ':
                entrada.arriba.caracter = '='
                entrada = entrada.arriba
            elif entrada.abajo != None and entrada.abajo.caracter == ' ':
                entrada.abajo.caracter = '='
                entrada = entrada.abajo
            elif entrada.abajo != None and entrada.abajo.caracter == 'C':
                entrada.abajo.caracter = 'C'
                entrada = entrada.abajo
            elif entrada.arriba != None and entrada.arriba.caracter == 'C':
                entrada.arriba.caracter = 'C'
                entrada = entrada.arriba
            elif entrada.izquierda != None and entrada.izquierda.caracter == 'C':
                entrada.izquierda.caracter = 'C'
                entrada = entrada.izquierda
            elif entrada.derecha != None and entrada.derecha.caracter == 'C':
                entrada.derecha.caracter = 'C'
                entrada = entrada.derecha
            elif entrada.derecha != None and entrada.derecha.caracter == ' ':
                entrada.derecha.caracter = '='
                entrada = entrada.derecha
            #Regresos
            elif entrada.izquierda != None  and entrada.izquierda.caracter != ' ':
                entrada.caracter = '$'
                #entrada.izquierda.caracter = '$'
                entrada = entrada.derecha
            elif entrada.derecha != None  and entrada.derecha.caracter != ' ':
                entrada.caracter = '$'
                #entrada.derecha.caracter = '$'
                entrada = entrada.izquierda
            elif entrada.arriba != None  and entrada.arriba.caracter != ' ':
                entrada.caracter = '$'
                #entrada.abajo.caracter = '$'
                entrada = entrada.abajo
            elif entrada.abajo != None  and entrada.abajo.caracter != ' ':
                entrada.caracter = '$'
                #entrada.arriba.caracter = '$'
                entrada = entrada.arriba
            #Regresos no camino
            elif entrada.derecha != None  and entrada.derecha.caracter == '*':
                entrada.caracter = '$'
                #entrada.izquierda.caracter = '$'
                entrada = entrada.izquierda
            elif entrada.izquierda != None  and entrada.izquierda.caracter == '*':
                entrada.caracter = '$'
                #entrada.derecha.caracter = '$'
                entrada = entrada.derecha
            elif entrada.arriba != None  and entrada.arriba.caracter == '*':
                entrada.caracter = '$'
                #entrada.abajo.caracter = '$'
                entrada = entrada.abajo
            elif entrada.abajo != None  and entrada.abajo.caracter == '*':
                entrada.caracter = '$'
                #entrada.arriba.caracter = '$'
                entrada = entrada.arriba
            elif entrada.derecha != None  and entrada.derecha.caracter == 'R':
                entrada.caracter = '$'
                #entrada.izquierda.caracter = '$'
                entrada = entrada.izquierda
            elif entrada.izquierda != None  and entrada.izquierda.caracter == 'R':
                entrada.caracter = '$'
                #entrada.derecha.caracter = '$'
                entrada = entrada.derecha
            elif entrada.arriba != None  and entrada.arriba.caracter == 'R':
                entrada.caracter = '$'
                #entrada.abajo.caracter = '$'
                entrada = entrada.abajo
            elif entrada.abajo != None  and entrada.abajo.caracter == 'R':
                entrada.caracter = '$'
                #entrada.arriba.caracter = '$'
                entrada = entrada.arriba

        #Arriba - derecha
        elif entrada != None and entrada.coordenadaX <= Civilfinal.coordenadaX and entrada.coordenadaY >= Civilfinal.coordenadaY :
            if entrada.abajo != None and entrada.abajo.caracter == ' ':
                entrada.abajo.caracter = '='
                entrada = entrada.abajo
            elif entrada.izquierda != None and entrada.izquierda.caracter == ' ':
                entrada.izquierda.caracter = '='
                entrada = entrada.izquierda
            elif entrada.arriba != None and entrada.arriba.caracter == ' ':
                entrada.arriba.caracter = '='
                entrada = entrada.arriba
            elif entrada.abajo != None and entrada.abajo.caracter == 'C':
                entrada.abajo.caracter = 'C'
                entrada = entrada.abajo
            elif entrada.arriba != None and entrada.arriba.caracter == 'C':
                entrada.arriba.caracter = 'C'
                entrada = entrada.arriba
            elif entrada.izquierda != None and entrada.izquierda.caracter == 'C':
                entrada.izquierda.caracter = 'C'
                entrada = entrada.izquierda
            elif entrada.derecha != None and entrada.derecha.caracter == 'C':
                entrada.derecha.caracter = 'C'
                entrada = entrada.derecha
            elif entrada.derecha != None and entrada.derecha.caracter == ' ':
                entrada.derecha.caracter = '='
                entrada = entrada.derecha
            #Regresos
            elif entrada.abajo != None  and entrada.abajo.caracter != ' ':
                entrada.caracter = '$'
                #entrada.izquierda.caracter = '$'
                entrada = entrada.arriba
            elif entrada.derecha != None  and entrada.derecha.caracter != ' ':
                entrada.caracter = '$'
                #entrada.derecha.caracter = '$'
                entrada = entrada.izquierda
            elif entrada.izquierda != None  and entrada.izquierda.caracter != ' ':
                entrada.caracter = '$'
                #entrada.abajo.caracter = '$'
                entrada = entrada.derecha
            elif entrada.arriba != None  and entrada.arriba.caracter != ' ':
                entrada.caracter = '$'
                #entrada.arriba.caracter = '$'
                entrada = entrada.abajo
            #Regresos no camino
            elif entrada.derecha != None  and entrada.derecha.caracter == '*':
                entrada.caracter = '$'
                #entrada.izquierda.caracter = '$'
                entrada = entrada.izquierda
            elif entrada.izquierda != None  and entrada.izquierda.caracter == '*':
                entrada.caracter = '$'
                #entrada.derecha.caracter = '$'
                entrada = entrada.derecha
            elif entrada.arriba != None  and entrada.arriba.caracter == '*':
                entrada.caracter = '$'
                #entrada.abajo.caracter = '$'
                entrada = entrada.abajo
            elif entrada.abajo != None  and entrada.abajo.caracter == '*':
                entrada.caracter = '$'
                #entrada.arriba.caracter = '$'
                entrada = entrada.arriba
            elif entrada.derecha != None  and entrada.derecha.caracter == 'R':
                entrada.caracter = '$'
                #entrada.izquierda.caracter = '$'
                entrada = entrada.izquierda
            elif entrada.izquierda != None  and entrada.izquierda.caracter == 'R':
                entrada.caracter = '$'
                #entrada.derecha.caracter = '$'
                entrada = entrada.derecha
            elif entrada.arriba != None  and entrada.arriba.caracter == 'R':
                entrada.caracter = '$'
                #entrada.abajo.caracter = '$'
                entrada = entrada.abajo
            elif entrada.abajo != None  and entrada.abajo.caracter == 'R':
                entrada.caracter = '$'
                #entrada.arriba.caracter = '$'
                entrada = entrada.arriba


        #Abajo - izquierda
        elif entrada != None and entrada.coordenadaX >= Civilfinal.coordenadaX and entrada.coordenadaY <= Civilfinal.coordenadaY :
            if entrada.arriba != None and entrada.arriba.caracter == ' ':
                entrada.arriba.caracter = '='
                entrada = entrada.arriba
            elif entrada.derecha != None and entrada.derecha.caracter == ' ':
                entrada.derecha.caracter = '='
                entrada = entrada.derecha
            elif entrada.izquierda != None and entrada.izquierda.caracter == ' ':
                entrada.izquierda.caracter = '='
                entrada = entrada.izquierda
            elif entrada.abajo != None and entrada.abajo.caracter == ' ':
                entrada.abajo.caracter = '='
                entrada = entrada.abajo
            elif entrada.abajo != None and entrada.abajo.caracter == 'C':
                entrada.abajo.caracter = 'C'
                entrada = entrada.abajo
            elif entrada.arriba != None and entrada.arriba.caracter == 'C':
                entrada.arriba.caracter = 'C'
                entrada = entrada.arriba
            elif entrada.izquierda != None and entrada.izquierda.caracter == 'C':
                entrada.izquierda.caracter = 'C'
                entrada = entrada.izquierda
            elif entrada.derecha != None and entrada.derecha.caracter == 'C':
                entrada.derecha.caracter = 'C'
                entrada = entrada.derecha
            #Regresos
            elif entrada.arriba != None  and entrada.arriba.caracter != ' ':
                entrada.caracter = '$'
                #entrada.izquierda.caracter = '$'
                entrada = entrada.abajo
            elif entrada.derecha != None  and entrada.derecha.caracter != ' ':
                entrada.caracter = '$'
                #entrada.derecha.caracter = '$'
                entrada = entrada.izquierda
            elif entrada.izquierda != None  and entrada.izquierda.caracter != ' ':
                entrada.caracter = '$'
                #entrada.abajo.caracter = '$'
                entrada = entrada.derecha
            elif entrada.abajo != None  and entrada.abajo.caracter != ' ':
                entrada.caracter = '$'
                #entrada.arriba.caracter = '$'
                entrada = entrada.arriba
            #Regresos no camino
            elif entrada.derecha != None  and entrada.derecha.caracter == '*':
                entrada.caracter = '$'
                #entrada.izquierda.caracter = '$'
                entrada = entrada.izquierda
            elif entrada.izquierda != None  and entrada.izquierda.caracter == '*':
                entrada.caracter = '$'
                #entrada.derecha.caracter = '$'
                entrada = entrada.derecha
            elif entrada.arriba != None  and entrada.arriba.caracter == '*':
                entrada.caracter = '$'
                #entrada.abajo.caracter = '$'
                entrada = entrada.abajo
            elif entrada.abajo != None  and entrada.abajo.caracter == '*':
                entrada.caracter = '$'
                #entrada.arriba.caracter = '$'
                entrada = entrada.arriba

        else:
            print(" ¡¡ MISION IMPOSIBLE !!")
            print("La misión no pudo ser completada")
            return False
            break


    
    
        


def misionRecurso(entrada):
    global capacidadfinal
    ciudad.limpiarRecurso()
    capacidadfinal = capacidadpelea
    print("Entra en el recorrido la entrada")  
    #ciudad.buscarEntrada()
    #entrada = ciudad.buscarEntrada()
    llega = False
    while llega is False:
        if entrada != None and entrada.arriba == RecursoFinal:
            llega = True
            ciudad.graficarNeatoR2(ciudad.nombre, ciudad, nombrerobot1, coordenadax, coordenaday, capacidadpelea, capacidadfinal)
            return True
            break     
        elif entrada != None and entrada.izquierda == RecursoFinal:
            llega = True
            ciudad.graficarNeatoR2(ciudad.nombre, ciudad, nombrerobot1, coordenadax, coordenaday, capacidadpelea, capacidadfinal)
            return True
            break
        elif entrada != None and entrada.derecha == RecursoFinal:
            llega = True
            ciudad.graficarNeatoR2(ciudad.nombre, ciudad, nombrerobot1, coordenadax, coordenaday, capacidadpelea, capacidadfinal)
            return True
            break
        elif entrada != None and entrada.abajo == RecursoFinal:
            llega = True
            ciudad.graficarNeatoR2(ciudad.nombre, ciudad, nombrerobot1, coordenadax, coordenaday, capacidadpelea, capacidadfinal)
            return True
            break


        #Arriba - izquierda
        elif entrada != None and entrada.coordenadaY <= RecursoFinal.coordenadaY and entrada.coordenadaX <= RecursoFinal.coordenadaX:
            if entrada.derecha != None and entrada.derecha.caracter == ' ':
                entrada.derecha.caracter = '='
                entrada = entrada.derecha
            elif entrada.abajo != None and entrada.abajo.caracter == ' ':
                entrada.abajo.caracter = '='
                entrada = entrada.abajo
            elif entrada.abajo != None and entrada.abajo.caracter == 'C':
                entrada.abajo.caracter = 'C'
                entrada = entrada.abajo
            elif entrada.arriba != None and entrada.arriba.caracter == 'C':
                entrada.arriba.caracter = 'C'
                entrada = entrada.arriba
            elif entrada.izquierda != None and entrada.izquierda.caracter == 'C':
                entrada.izquierda.caracter = 'C'
                entrada = entrada.izquierda
            elif entrada.derecha != None and entrada.derecha.caracter == 'C':
                entrada.derecha.caracter = 'C'
                entrada = entrada.derecha
            elif entrada.arriba != None and entrada.arriba.caracter == ' ':
                entrada.arriba.caracter = '='
                entrada = entrada.arriba            
            elif entrada.izquierda != None and entrada.izquierda.caracter == ' ':
                entrada.izquierda.caracter = '='
                entrada = entrada.izquierda
            # elif (entrada.derecha != None and entrada.derecha.caracter == 'UM'
            # and unidades.buscarUnidad1(entrada.derecha.posx, entrada.derecha.posy) != False
            # and int(unidades.buscarUnidad1(entrada.derecha.posx, entrada.derecha.posy)).getCapacidad() <= int(capacidadpelea)):
            #     capacidadfinal = int(capacidadpelea) - int((unidades.buscarUnidad1(entrada.derecha.posx, entrada.derecha.posy)).getCapacidad())
            #     entrada.derecha.carcter = '='
            #     entrada = entrada.derecha
            # # elif entrada.derecha != None and entrada.derecha.caracter == 'UM' and unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) != False and int(unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY).getCapacidad() <= int(capacidadpelea)) :
            #     capacidadfinal = capacidadpelea - unidades.buscarUnidad1(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) 
            #     entrada.derecha.caracter = '='
            #     entrada = entrada.derecha
            # elif entrada.arriba != None and entrada.arriba.caracter == 'UM' and unidades.buscarUnidad(entrada.arriba.coordenadaX, entrada.arriba.coordenadaY) != False and int(unidades.buscarUnidad(entrada.arriba.coordenadaX, entrada.arriba.coordenadaY).getCapacidad() <= int(capacidadpelea)) :
            #     capacidadfinal = capacidadpelea - unidades.buscarUnidad1(entrada.arriba.coordenadaX, entrada.arriba.coordenadaY) 
            #     entrada.arriba.caracter = '='
            #     entrada = entrada.arriba
            # elif entrada.abajo != None and entrada.abajo.caracter == 'UM' and unidades.buscarUnidad(entrada.abajo.coordenadaX, entrada.abajo.coordenadaY) != False and int(unidades.buscarUnidad(entrada.abajo.coordenadaX, entrada.abajo.coordenadaY).getCapacidad() <= int(capacidadpelea)) :
            #     capacidadfinal = capacidadpelea - unidades.buscarUnidad1(entrada.abajo.coordenadaX, entrada.abajo.coordenadaY) 
            #     entrada.abajo.caracter = '='
            #     entrada = entrada.abajo
            # elif entrada.izquierda != None and entrada.izquierda.caracter == 'UM' and unidades.buscarUnidad(entrada.izquierda.coordenadaX, entrada.izquierda.coordenadaY) != False and int(unidades.buscarUnidad(entrada.izquierda.coordenadaX, entrada.izquierda.coordenadaY).getCapacidad() <= int(capacidadpelea)) :
            #     capacidadfinal = capacidadpelea - unidades.buscarUnidad1(entrada.izquierda.coordenadaX, entrada.izquierda.coordenadaY) 
            #     entrada.izquierda.caracter = '='
            #     entrada = entrada.izquierda
            # #Regresos
            elif entrada.derecha != None  and entrada.derecha.caracter != ' ':
                entrada.caracter = '$'
                #entrada.izquierda.caracter = '$'
                entrada = entrada.izquierda
            elif entrada.izquierda != None  and entrada.izquierda.caracter != ' ':
                entrada.caracter = '$'
                #entrada.derecha.caracter = '$'
                entrada = entrada.derecha
            elif entrada.arriba != None  and entrada.arriba.caracter != ' ':
                entrada.caracter = '$'
                #entrada.abajo.caracter = '$'
                entrada = entrada.abajo
            elif entrada.abajo != None  and entrada.abajo.caracter != ' ':
                entrada.caracter = '$'
                #entrada.arriba.caracter = '$'
                entrada = entrada.arriba
            #Regreso de no camino
            # elif entrada.derecha != None  and entrada.derecha.caracter == '*':
            #     entrada.caracter = '$'
            #     #entrada.izquierda.caracter = '$'
            #     entrada = entrada.izquierda
            # elif entrada.izquierda != None  and entrada.izquierda.caracter == '*':
            #     entrada.caracter = '$'
            #     #entrada.derecha.caracter = '$'
            #     entrada = entrada.derecha
            # elif entrada.arriba != None  and entrada.arriba.caracter == '*':
            #     entrada.caracter = '$'
            #     #entrada.abajo.caracter = '$'
            #     entrada = entrada.abajo
            # elif entrada.abajo != None  and entrada.abajo.caracter == '*':
            #     entrada.caracter = '$'
            #     #entrada.arriba.caracter = '$'
            #     entrada = entrada.arriba
            # # elif entrada.derecha != None and entrada.derecha.caracter == 'UM' and unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) >= capacidadpelea:
            #     #capacidadfinal = unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) - capacidadpelea
            #     entrada.izquierda.caracter = '='
            #     entrada = entrada.izquierda
            # elif entrada.izquierda != None and entrada.izquierda.caracter == 'UM' and unidades.buscarUnidad(entrada.izquierda.coordenadaX, entrada.izquierda.coordenadaY) >= capacidadpelea:
            #     #capacidadfinal = unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) - capacidadpelea
            #     entrada.derecha.caracter = '='
            #     entrada = entrada.derecha
            # elif entrada.arriba != None and entrada.arriba.caracter == 'UM' and unidades.buscarUnidad(entrada.arriba.coordenadaX, entrada.arriba.coordenadaY) >= capacidadpelea:
            #     #capacidadfinal = unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) - capacidadpelea
            #     entrada.abajo.caracter = '='
            #     entrada = entrada.abajo
            # elif entrada.abajo != None and entrada.abajo.caracter == 'UM' and unidades.buscarUnidad(entrada.abajo.coordenadaX, entrada.abajo.coordenadaY) >= capacidadpelea:
            #     #capacidadfinal = unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) - capacidadpelea
            #     entrada.arriba.caracter = '='
            #     entrada = entrada.arriba
            


        #Abajo - Derecha
        elif entrada != None and entrada.coordenadaY >= RecursoFinal.coordenadaY and entrada.coordenadaX >= RecursoFinal.coordenadaX:
            if entrada.izquierda != None and entrada.izquierda.caracter == ' ':
                entrada.izquierda.caracter = '='
                entrada = entrada.izquierda
            elif entrada.arriba != None and entrada.arriba.caracter == ' ':
                entrada.arriba.caracter = '='
                entrada = entrada.arriba
            elif entrada.abajo != None and entrada.abajo.caracter == ' ':
                entrada.abajo.caracter = '='
                entrada = entrada.abajo
            elif entrada.abajo != None and entrada.abajo.caracter == 'C':
                entrada.abajo.caracter = 'C'
                entrada = entrada.abajo
            elif entrada.arriba != None and entrada.arriba.caracter == 'C':
                entrada.arriba.caracter = 'C'
                entrada = entrada.arriba
            elif entrada.izquierda != None and entrada.izquierda.caracter == 'C':
                entrada.izquierda.caracter = 'C'
                entrada = entrada.izquierda
            elif entrada.derecha != None and entrada.derecha.caracter == 'C':
                entrada.derecha.caracter = 'C'
                entrada = entrada.derecha
            elif entrada.derecha != None and entrada.derecha.caracter == ' ':
                entrada.derecha.caracter = '='
                entrada = entrada.derecha
            # elif entrada.derecha != None and entrada.derecha.caracter == 'UM' and unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) != False and int(unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY).getCapacidad() <= int(capacidadpelea)) :
            #     capacidadfinal = capacidadpelea - unidades.buscarUnidad1(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) 
            #     entrada.derecha.caracter = '='
            #     entrada = entrada.derecha
            # elif entrada.arriba != None and entrada.arriba.caracter == 'UM' and unidades.buscarUnidad(entrada.arriba.coordenadaX, entrada.arriba.coordenadaY) != False and int(unidades.buscarUnidad(entrada.arriba.coordenadaX, entrada.arriba.coordenadaY).getCapacidad() <= int(capacidadpelea)) :
            #     capacidadfinal = capacidadpelea - unidades.buscarUnidad1(entrada.arriba.coordenadaX, entrada.arriba.coordenadaY) 
            #     entrada.arriba.caracter = '='
            #     entrada = entrada.arriba
            # elif entrada.abajo != None and entrada.abajo.caracter == 'UM' and unidades.buscarUnidad(entrada.abajo.coordenadaX, entrada.abajo.coordenadaY) != False and int(unidades.buscarUnidad(entrada.abajo.coordenadaX, entrada.abajo.coordenadaY).getCapacidad() <= int(capacidadpelea)) :
            #     capacidadfinal = capacidadpelea - unidades.buscarUnidad1(entrada.abajo.coordenadaX, entrada.abajo.coordenadaY) 
            #     entrada.abajo.caracter = '='
            #     entrada = entrada.abajo
            # elif entrada.izquierda != None and entrada.izquierda.caracter == 'UM' and unidades.buscarUnidad(entrada.izquierda.coordenadaX, entrada.izquierda.coordenadaY) != False and int(unidades.buscarUnidad(entrada.izquierda.coordenadaX, entrada.izquierda.coordenadaY).getCapacidad() <= int(capacidadpelea)) :
            #     capacidadfinal = capacidadpelea - unidades.buscarUnidad1(entrada.izquierda.coordenadaX, entrada.izquierda.coordenadaY) 
            #     entrada.izquierda.caracter = '='
            #     entrada = entrada.izquierda
            # # #Regresos
            elif entrada.izquierda != None  and entrada.izquierda.caracter != ' ':
                entrada.caracter = '$'
                #entrada.izquierda.caracter = '$'
                entrada = entrada.derecha
            elif entrada.derecha != None  and entrada.derecha.caracter != ' ':
                entrada.caracter = '$'
                #entrada.derecha.caracter = '$'
                entrada = entrada.izquierda
            elif entrada.arriba != None  and entrada.arriba.caracter != ' ':
                entrada.caracter = '$'
                #entrada.abajo.caracter = '$'
                entrada = entrada.abajo
            elif entrada.abajo != None  and entrada.abajo.caracter != ' ':
                entrada.caracter = '$'
                #entrada.arriba.caracter = '$'
                entrada = entrada.arriba
            #Regresos no camino
            # elif entrada.derecha != None  and entrada.derecha.caracter == '*':
            #     entrada.caracter = '$'
            #     #entrada.izquierda.caracter = '$'
            #     entrada = entrada.izquierda
            # elif entrada.izquierda != None  and entrada.izquierda.caracter == '*':
            #     entrada.caracter = '$'
            #     #entrada.derecha.caracter = '$'
            #     entrada = entrada.derecha
            # elif entrada.arriba != None  and entrada.arriba.caracter == '*':
            #     entrada.caracter = '$'
            #     #entrada.abajo.caracter = '$'
            #     entrada = entrada.abajo
            # elif entrada.abajo != None  and entrada.abajo.caracter == '*':
            #     entrada.caracter = '$'
            #     #entrada.arriba.caracter = '$'
            #     entrada = entrada.arriba
            # # elif entrada.derecha != None and entrada.derecha.caracter == 'UM' and unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) >= capacidadpelea:
            #     #capacidadfinal = unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) - capacidadpelea
            #     entrada.izquierda.caracter = '='
            #     entrada = entrada.izquierda
            # elif entrada.izquierda != None and entrada.izquierda.caracter == 'UM' and unidades.buscarUnidad(entrada.izquierda.coordenadaX, entrada.izquierda.coordenadaY) >= capacidadpelea:
            #     #capacidadfinal = unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) - capacidadpelea
            #     entrada.derecha.caracter = '='
            #     entrada = entrada.derecha
            # elif entrada.arriba != None and entrada.arriba.caracter == 'UM' and unidades.buscarUnidad(entrada.arriba.coordenadaX, entrada.arriba.coordenadaY) >= capacidadpelea:
            #     #capacidadfinal = unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) - capacidadpelea
            #     entrada.abajo.caracter = '='
            #     entrada = entrada.abajo
            # elif entrada.abajo != None and entrada.abajo.caracter == 'UM' and unidades.buscarUnidad(entrada.abajo.coordenadaX, entrada.abajo.coordenadaY) >= capacidadpelea:
            #     #capacidadfinal = unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) - capacidadpelea
            #     entrada.arriba.caracter = '='
            #     entrada = entrada.arriba
            

        #Arriba - derecha
        elif entrada != None and entrada.coordenadaX <= RecursoFinal.coordenadaX and entrada.coordenadaY >= RecursoFinal.coordenadaY :
            if entrada.abajo != None and entrada.abajo.caracter == ' ':
                entrada.abajo.caracter = '='
                entrada = entrada.abajo
            elif entrada.izquierda != None and entrada.izquierda.caracter == ' ':
                entrada.izquierda.caracter = '='
                entrada = entrada.izquierda
            elif entrada.arriba != None and entrada.arriba.caracter == ' ':
                entrada.arriba.caracter = '='
                entrada = entrada.arriba
            elif entrada.abajo != None and entrada.abajo.caracter == 'C':
                entrada.abajo.caracter = 'C'
                entrada = entrada.abajo
            elif entrada.arriba != None and entrada.arriba.caracter == 'C':
                entrada.arriba.caracter = 'C'
                entrada = entrada.arriba
            elif entrada.izquierda != None and entrada.izquierda.caracter == 'C':
                entrada.izquierda.caracter = 'C'
                entrada = entrada.izquierda
            elif entrada.derecha != None and entrada.derecha.caracter == 'C':
                entrada.derecha.caracter = 'C'
                entrada = entrada.derecha
            elif entrada.derecha != None and entrada.derecha.caracter == ' ':
                entrada.derecha.caracter = '='
                entrada = entrada.derecha
            # elif entrada.derecha != None and entrada.derecha.caracter == 'UM' and unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) != False and int(unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY).getCapacidad() <= int(capacidadpelea)) :
            #     capacidadfinal = capacidadpelea - unidades.buscarUnidad1(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) 
            #     entrada.derecha.caracter = '='
            #     entrada = entrada.derecha
            # elif entrada.arriba != None and entrada.arriba.caracter == 'UM' and unidades.buscarUnidad(entrada.arriba.coordenadaX, entrada.arriba.coordenadaY) != False and int(unidades.buscarUnidad(entrada.arriba.coordenadaX, entrada.arriba.coordenadaY).getCapacidad() <= int(capacidadpelea)) :
            #     capacidadfinal = capacidadpelea - unidades.buscarUnidad1(entrada.arriba.coordenadaX, entrada.arriba.coordenadaY) 
            #     entrada.arriba.caracter = '='
            #     entrada = entrada.arriba
            # elif entrada.abajo != None and entrada.abajo.caracter == 'UM' and unidades.buscarUnidad(entrada.abajo.coordenadaX, entrada.abajo.coordenadaY) != False and int(unidades.buscarUnidad(entrada.abajo.coordenadaX, entrada.abajo.coordenadaY).getCapacidad() <= int(capacidadpelea)) :
            #     capacidadfinal = capacidadpelea - unidades.buscarUnidad1(entrada.abajo.coordenadaX, entrada.abajo.coordenadaY) 
            #     entrada.abajo.caracter = '='
            #     entrada = entrada.abajo
            # elif entrada.izquierda != None and entrada.izquierda.caracter == 'UM' and unidades.buscarUnidad(entrada.izquierda.coordenadaX, entrada.izquierda.coordenadaY) != False and int(unidades.buscarUnidad(entrada.izquierda.coordenadaX, entrada.izquierda.coordenadaY).getCapacidad() <= int(capacidadpelea)) :
            #     capacidadfinal = capacidadpelea - unidades.buscarUnidad1(entrada.izquierda.coordenadaX, entrada.izquierda.coordenadaY) 
            #     entrada.izquierda.caracter = '='
            #     entrada = entrada.izquierda
            # # #Regresos
            elif entrada.abajo != None  and entrada.abajo.caracter != ' ':
                entrada.caracter = '$'
                #entrada.izquierda.caracter = '$'
                entrada = entrada.arriba
            elif entrada.derecha != None  and entrada.derecha.caracter != ' ':
                entrada.caracter = '$'
                #entrada.derecha.caracter = '$'
                entrada = entrada.izquierda
            elif entrada.izquierda != None  and entrada.izquierda.caracter != ' ':
                entrada.caracter = '$'
                #entrada.abajo.caracter = '$'
                entrada = entrada.derecha
            elif entrada.arriba != None  and entrada.arriba.caracter != ' ':
                entrada.caracter = '$'
                #entrada.arriba.caracter = '$'
                entrada = entrada.abajo
            #Regresos no camino
            # elif entrada.derecha != None  and entrada.derecha.caracter == '*':
            #     entrada.caracter = '$'
            #     #entrada.izquierda.caracter = '$'
            #     entrada = entrada.izquierda
            # elif entrada.izquierda != None  and entrada.izquierda.caracter == '*':
            #     entrada.caracter = '$'
            #     #entrada.derecha.caracter = '$'
            #     entrada = entrada.derecha
            # elif entrada.arriba != None  and entrada.arriba.caracter == '*':
            #     entrada.caracter = '$'
            #     #entrada.abajo.caracter = '$'
            #     entrada = entrada.abajo
            # elif entrada.abajo != None  and entrada.abajo.caracter == '*':
            #     entrada.caracter = '$'
            #     #entrada.arriba.caracter = '$'
            #     entrada = entrada.arriba
            # # elif entrada.derecha != None and entrada.derecha.caracter == 'UM' and unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) >= capacidadpelea:
            #     #capacidadfinal = unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) - capacidadpelea
            #     entrada.izquierda.caracter = '='
            #     entrada = entrada.izquierda
            # elif entrada.izquierda != None and entrada.izquierda.caracter == 'UM' and unidades.buscarUnidad(entrada.izquierda.coordenadaX, entrada.izquierda.coordenadaY) >= capacidadpelea:
            #     #capacidadfinal = unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) - capacidadpelea
            #     entrada.derecha.caracter = '='
            #     entrada = entrada.derecha
            # elif entrada.arriba != None and entrada.arriba.caracter == 'UM' and unidades.buscarUnidad(entrada.arriba.coordenadaX, entrada.arriba.coordenadaY) >= capacidadpelea:
            #     #capacidadfinal = unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) - capacidadpelea
            #     entrada.abajo.caracter = '='
            #     entrada = entrada.abajo
            # elif entrada.abajo != None and entrada.abajo.caracter == 'UM' and unidades.buscarUnidad(entrada.abajo.coordenadaX, entrada.abajo.coordenadaY) >= capacidadpelea:
            #     #capacidadfinal = unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) - capacidadpelea
            #     entrada.arriba.caracter = '='
            #     entrada = entrada.arriba


        #Abajo - izquierda
        elif entrada != None and entrada.coordenadaX >= RecursoFinal.coordenadaX and entrada.coordenadaY <= RecursoFinal.coordenadaY :
            if entrada.arriba != None and entrada.arriba.caracter == ' ':
                entrada.arriba.caracter = '='
                entrada = entrada.arriba
            elif entrada.derecha != None and entrada.derecha.caracter == ' ':
                entrada.derecha.caracter = '='
                entrada = entrada.derecha
            elif entrada.izquierda != None and entrada.izquierda.caracter == ' ':
                entrada.izquierda.caracter = '='
                entrada = entrada.izquierda
            elif entrada.abajo != None and entrada.abajo.caracter == ' ':
                entrada.abajo.caracter = '='
                entrada = entrada.abajo
            elif entrada.abajo != None and entrada.abajo.caracter == 'C':
                entrada.abajo.caracter = 'C'
                entrada = entrada.abajo
            elif entrada.arriba != None and entrada.arriba.caracter == 'C':
                entrada.arriba.caracter = 'C'
                entrada = entrada.arriba
            elif entrada.izquierda != None and entrada.izquierda.caracter == 'C':
                entrada.izquierda.caracter = 'C'
                entrada = entrada.izquierda
            elif entrada.derecha != None and entrada.derecha.caracter == 'C':
                entrada.derecha.caracter = 'C'
                entrada = entrada.derecha
            
            
            # #Regresos
            elif entrada.arriba != None  and entrada.arriba.caracter != ' ':
                entrada.caracter = '$'
                #entrada.izquierda.caracter = '$'
                entrada = entrada.abajo
            elif entrada.derecha != None  and entrada.derecha.caracter != ' ':
                entrada.caracter = '$'
                #entrada.derecha.caracter = '$'
                entrada = entrada.izquierda
            elif entrada.izquierda != None  and entrada.izquierda.caracter != ' ':
                entrada.caracter = '$'
                #entrada.abajo.caracter = '$'
                entrada = entrada.derecha
            elif entrada.abajo != None  and entrada.abajo.caracter != ' ':
                entrada.caracter = '$'
                #entrada.arriba.caracter = '$'
                entrada = entrada.arriba
            #Regresos no camino
            # elif entrada.derecha != None  and entrada.derecha.caracter == '*':
            #     entrada.caracter = '$'
            #     #entrada.izquierda.caracter = '$'
            #     entrada = entrada.izquierda
            # elif entrada.izquierda != None  and entrada.izquierda.caracter == '*':
            #     entrada.caracter = '$'
            #     #entrada.derecha.caracter = '$'
            #     entrada = entrada.derecha
            # elif entrada.arriba != None  and entrada.arriba.caracter == '*':
            #     entrada.caracter = '$'
            #     #entrada.abajo.caracter = '$'
            #     entrada = entrada.abajo
            # elif entrada.abajo != None  and entrada.abajo.caracter == '*':
            #     entrada.caracter = '$'
            #     #entrada.arriba.caracter = '$'
            #     entrada = entrada.arriba
            # # elif entrada.derecha != None and entrada.derecha.caracter == 'UM' and unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) >= capacidadpelea:
            #     #capacidadfinal = unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) - capacidadpelea
            #     entrada.izquierda.caracter = '='
            #     entrada = entrada.izquierda
            # elif entrada.izquierda != None and entrada.izquierda.caracter == 'UM' and unidades.buscarUnidad(entrada.izquierda.coordenadaX, entrada.izquierda.coordenadaY) >= capacidadpelea:
            #     #capacidadfinal = unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) - capacidadpelea
            #     entrada.derecha.caracter = '='
            #     entrada = entrada.derecha
            # elif entrada.arriba != None and entrada.arriba.caracter == 'UM' and unidades.buscarUnidad(entrada.arriba.coordenadaX, entrada.arriba.coordenadaY) >= capacidadpelea:
            #     #capacidadfinal = unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) - capacidadpelea
            #     entrada.abajo.caracter = '='
            #     entrada = entrada.abajo
            # elif entrada.abajo != None and entrada.abajo.caracter == 'UM' and unidades.buscarUnidad(entrada.abajo.coordenadaX, entrada.abajo.coordenadaY) >= capacidadpelea:
            #     #capacidadfinal = unidades.buscarUnidad(entrada.derecha.coordenadaX, entrada.derecha.coordenadaY) - capacidadpelea
            #     entrada.arriba.caracter = '='
            #     entrada = entrada.arriba

        else:
            print(" ¡¡ MISION IMPOSIBLE !!")
            print("La misión no pudo ser completada")
            return False
            break


def insertaTodo():
    #try:
        global nuevonombre
        
        print("")
        print("---Ciudades Disponibles para graficar---")
        print("")
        time.sleep(0.5)
        if ciudades.largo  == 0:
            print("No hay Ciudades ingresados")
        else:
            #for i in range (1, ciudades.largo+1):
            #    print("- ", ciudades.getCiudad(i).nombre)
            ciudades.mostrarElementos()
            print("")
            print("Escriba el nombre de la Ciudad a graficar:")
            nombreCiudad = input("- ")
            matriz = ciudades.buscarCiudad(nombreCiudad)
            if matriz is None:
                print("")
                print("¡Error!")
                print("La ciudad ingresada no existe")
                print("")
            else:
                print("Nombre elegido: ", nombreCiudad)
                print("")
                print("Generando grafica.........")
                print("")
                time.sleep(0.5)
                with open("Salida/" + nombreCiudad + ".txt") as archivo:
                #with open(nombreCiudad + ".txt") as archivo:
                    l = 0
                    c = 0
                    lineas = archivo.readlines()
                    for linea in lineas:
                        columnas = linea.replace('"','')
                        l += 1
                        for col in columnas:
                            if col != '\n':
                                c += 1
                                matriz.insert(l, c, col)
                        c = 0
                        matriz.graficarNeatoR(nombreCiudad, matriz)
                #nuevonombre = "matriz_"+nombreCiudad
                print("Ciudad Grafica con exito")
                webbrowser.open("matriz_"+ nombreCiudad + ".pdf")
    #except:
    #    print("")
    #    print("Vuelva a elegir una opcion")

def buscarciudad():
    global matriz
    global nombreCiudad
    try:
        print("")
        print("---Ciudades Disponibles---")
        print("")
        time.sleep(0.5)
        if ciudades.largo  == 0:
            print("No hay Ciudades ingresados")
        else:
            #for i in range (1, ciudades.largo+1):
            #    print("- ", ciudades.getCiudad(i).nombre)
            ciudades.mostrarElementos()
            print("")
            print("Escriba el nombre de la Ciudad para realizar una misión:")
            nombreCiudad = input("- ")
            matriz = ciudades.buscarCiudad(nombreCiudad)
            if matriz is None:
                print("")
                print("¡Error!")
                print("La ciudad ingresada no existe")
                print("")
            else:
                print("")
                time.sleep(0.5)
                with open("Salida/" + nombreCiudad + ".txt") as archivo:
                    l = 0
                    c = 0
                    lineas = archivo.readlines()
                    for linea in lineas:
                        columnas = linea.replace('"','')
                        l += 1
                        for col in columnas:
                            if col != '\n':
                                c += 1
                                matriz.insert(l, c, col)
                        c = 0
                        matriz.graficarNeatoR(nombreCiudad, matriz)
    except:
        print("")
        print("Vuelva a elegir una opcion")
    return matriz


def menu():
    opcion = ''
    while opcion != '4':
        print("------Menu principal------")
        print("1. Cargar Ciudades")
        print("2. Realizar Misiones")
        print("3. Graficar Ciudad")
        print("4. Salida")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            cargarArchivo1()
        elif opcion == '2':
            realizarmision()
            print("")
        elif opcion == '3':
            insertaTodo()
            print("")
        elif opcion != "4":
            print("Ingrese una opcion correcta" +"\n" )
        else:
            print("Gracias por usar nuestro programa :D")
            break

menu()      