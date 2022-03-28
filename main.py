from re import sub
import xml.etree.ElementTree as ET
from listaSimpleCiudad import ListaSimple as listaciudad
import graphviz
import time
from MatrizDispersa import MatrizDispersa
import webbrowser

matriz = MatrizDispersa(0)

capacidad_combate = 0
ciudades = listaciudad()


archivoEntrada = None
rutaEntrada = None


def cargarArchivo():
    global archivoEntrada
    global rutaEntrada
    global ciudades 
    
    print("---------- Cargar Archivo ----------")
    Filename = input('Ingrese la ruta del archivo: ')
    file = Filename

    if str(file).endswith('.xml'):
        try:
            archivoEntrada = ET.parse(file)
            rutaEntrada = archivoEntrada.getroot()

            print(" El archivo se cargó con éxito ")
            print("")

            print("Analizando archivo...")

            for elemento in rutaEntrada:
                for subelemento in elemento:
                    if subelemento.tag == 'ciudad': 
                        for subelemento1 in subelemento:
                            if subelemento1.tag == 'nombre':
                                doc = open("Salida/" + subelemento1.text + ".txt", "w")
                                nombre = subelemento1.text    
                                ciudades.agregar(nombre)  
                            if subelemento1.tag == 'fila':
                                doc.write(subelemento1.text + '\n')
                            #if subelemento1.tag == 'unidadMilitar':
                            #    ciudades.agregarUnidad(subelemento1.attrib['fila'], subelemento1.attrib['columna'], subelemento1.text)
                        doc.close()


            for elemento in rutaEntrada.find('robots'):
                for subelemento2 in elemento:
                    if subelemento2.tag == 'robot':
                        for subelemento3 in subelemento2:
                            if subelemento3.tag == 'nombre':
                                tipo = subelemento3.attrib['tipo']
                                capacidad_combate = subelemento3.attrib['capacidad']
                                nombre_r = subelemento3.text
                                
            '''for elemento2 in rutaEntrada:
                for subelemento2 in elemento2:
                    if subelemento2.tag == 'robot':
                        for subelemento3 in subelemento2:
                            if subelemento3.tag == 'nombre':
                                tipo = subelemento3.attrib['tipo']
                                capacidad_combate = subelemento3.attrib['capacidad']
                                nombre_r = subelemento3.text
                                ciudades.agregarRobot(tipo,capacidad_combate,nombre_r) '''
                

            #print(prueba)

            print("")
            print("-----Ciudades encontradas -----")
            print("")
            #ciudades.mostrarUnidad()
            ciudades.mostrarElementos() 
            print("----Robots encontrados----") 
            ciudades.mostrarRobot()         
            time.sleep(0.5)
        except:
            print("")
            print("¡¡ ERROR !!")
            print("El archivo proporcionado no cumple con los estándares de las ciudades")

    else:
        print("¡¡ ERROR !!")
        print("El archivo cargado no es compatible con un .xml")

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
            Ciudad = ciudades.buscarCiudad(nombreCiudad)
            if Ciudad is None:
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
                matriz.graficarNeato(nombreCiudad)
                nuevonombre = "matriz_"+nombreCiudad
        print("Ciudad Grafica con exito")
        #webbrowser.open_new_tab('Prueba/'+ nuevonombre + ".pdf")
        #webbrowser.open_new_tab(nuevonombre + ".pdf")
    except:
        print("")
        print("Vuelva a elegir una opcion")


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
            #procesararchivo()
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