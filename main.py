import gc
import xml.etree.ElementTree as ET
from listaSimpleCiudad import ListaSimple as listaciudad
from Lista_UM import Lista_UM
from Lista_Robots import Lista_Robots
import graphviz
import time
from MatrizDispersa import MatrizDispersa
import webbrowser

capacidad_combate = 0
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
                                #doc = open("Salida/" + subelemento1.text + ".txt", "w")
                                doc = open(subelemento1.text + ".txt", "w")
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
                            print(robots.largoRobot)


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
            print("Ha ocurrido un erorr en la carga del archivo")

    else:
        print("¡¡ ERROR !!")
        print("El archivo cargado no es compatible con un .xml")



def realizarmision():
    ciudad = buscarciudad()
    print("")
    print("Misiones Disponibles")
    print("1. Rescate")
    print("2. Extracción de recursos")
    print("")
    nombremision = input("Elija una opcion: ")
    if nombremision == '1':
        print("Mision de Rescate")
        print("")
        print("-----Robots Disponibles-----""\n")
        if robots.obtenerTipoRescue() == 0:
        
            print("No existen robots para esta misión")
        else:
            nombrerobot = input("\n""Escriba el nombre del robot - ")
            if robots.buscarRobotmision(nombrerobot, 'ChapinRescue') != False:
                print("Si existe")

                print(ciudad.getUnidadesCiviles())
            else:
                print("El robot no ha sido encontrado")
            
    if nombremision == '2':
        print("Mision de Extracción de Recursos")
        print("")
        print("-----Robots Disponibles-----")
        if robots.obtenerTipoFighter() == 0:
            print("No existen robots para esta misión")
        else:
            nombrerobot1 = input("\n""Escriba el nombre del robot - ")
            if robots.buscarRobotmision(nombrerobot1, 'ChapinFighter') != False:
                print("Si existe")
            else:
                print("El robot no ha sido encontrado")



def insertaTodo():
    try:
        global nuevonombre
        
        print("")
        print(" Ciudades Disponibles para graficar")
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
        #with open("Salida/" + nombreCiudad + ".txt") as archivo:
                with open(nombreCiudad + ".txt") as archivo:
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
    try:
    
        print("")
        print(" Ciudades Disponibles para graficar")
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
                #print("Nombre elegido: ", nombreCiudad)
                print("")
                time.sleep(0.5)
                with open(nombreCiudad + ".txt") as archivo:
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
                #print("Ciudad Grafica con exito")
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