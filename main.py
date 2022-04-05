import xml.etree.ElementTree as ET
from listaSimpleCiudad import ListaSimple as listaciudad
from Lista_UM import Lista_UM
from Lista_Robots import Lista_Robots
import graphviz
import time
from MatrizDispersa import MatrizDispersa
import webbrowser

capacidad_combate = 99999
ciudades = listaciudad()
robots = Lista_Robots()


archivoEntrada = None
rutaEntrada = None


def cargarArchivo():
    global archivoEntrada
    global rutaEntrada
    global ciudades 
    global robots
    
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
                                doc = open("Salida/" + subelemento1.text + ".txt", "w")
                                #doc = open(subelemento1.text + ".txt", "w")
                            if subelemento1.tag == 'fila':
                                doc.write(subelemento1.text + '\n')
                            if subelemento1.tag == 'unidadMilitar':
                                unidades.agregarUnidad(subelemento1.attrib['fila'], subelemento1.attrib['columna'], subelemento1.text)
                        #ciudades.agregar(nombre, unidades)
                        ciudades.agregarMatriz(0, nombre, unidades)
                        
                        doc.close()
                    if subelemento.tag == 'robot':
                        for subelemento1 in subelemento:
                            if subelemento1.tag == 'nombre':
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
                    ciudad.mostrarRecurso()
                else:
                    print("El robot no ha sido encontrado")
        else:
            print("Lo sentimos, la ciudad no cuenta con recursos para completar la misión")


def recorrerciudad(ciudad):
    global Civilfinal
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

    


def misionCivil(entrada):
    ciudad.limpiar()
    print("entra a mision")  
    #ciudad.buscarEntrada()
    #entrada = ciudad.buscarEntrada()
    llega = False
    while llega is False:
        if entrada != None and entrada.arriba == Civilfinal:
            llega = True
            ciudad.graficarNeatoR1(ciudad.nombre, ciudad, nombrerobot)
            return True
            break     
        elif entrada != None and entrada.izquierda == Civilfinal:
            llega = True
            ciudad.graficarNeatoR1(ciudad.nombre, ciudad, nombrerobot)
            return True
            break
        elif entrada != None and entrada.derecha == Civilfinal:
            llega = True
            ciudad.graficarNeatoR1(ciudad.nombre, ciudad, nombrerobot)
            return True
            break
        elif entrada != None and entrada.abajo == Civilfinal:
            llega = True
            ciudad.graficarNeatoR1(ciudad.nombre, ciudad, nombrerobot)
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
            #elif entrada.derecha != None and entrada.derecha.caracter == 'UM':
            #    entrada.izquierda.


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

        
        

        else:
            print("Error, la misión no pudo ser completada")
            return False
            break


    
    
    #webbrowser.open("matriz_"+ ciudad.nombre + "_mision")




def insertaTodo():
    try:
        global nuevonombre
        
        print("")
        print("---Ciudades Disponibles para graficar---")
        print("")
        time.sleep(0.5)
        if ciudades.largo  == 0:
            print("No hay Ciudades ingresados")
        else:
            for i in range (1, ciudades.largo+1):
                print("- ", ciudades.getCiudad(i).nombre)
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
    except:
        print("")
        print("Vuelva a elegir una opcion")

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
            for i in range (1, ciudades.largo+1):
                print("- ", ciudades.getCiudad(i).nombre)
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
                #print("Nombre elegido: ", nombreCiudad)
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
    while opcion != '5':
        print("------Menu principal------")
        print("1. Cargar Ciudades")
        print("2. Realizar Misiones")
        print("3. Escribir archivo de salida")
        print("4. Graficar Ciudad")
        print("5. Salida")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            cargarArchivo()
        elif opcion == '2':
            realizarmision()
            print("")
        elif opcion == '3':
            print("Archivo de salida" +"\n" )
        elif opcion == '4':
            insertaTodo()
            #webbrowser.open("Grafico/" + nuevonombre + ".pdf")
            print("")
        elif opcion != "5":
            print("Ingrese una opcion correcta" +"\n" )
        else:
            print("Gracias por usar nuestro programa :D")
            break

menu()      