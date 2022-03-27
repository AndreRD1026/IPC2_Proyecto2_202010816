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
    #print("")
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
                        doc.close()

            print("")
            print("Ciudades encontradas")
            ciudades.mostrarElementos()           
            time.sleep(0.5)
        except:
            print("")
            print("¡¡ ERROR !!")
            print("El archivo proporcionado no cumple con los estándares de las ciudades")

    else:
        print("¡¡ ERROR !!")
        print("El archivo cargado no es compatible con un .xml")

def insertaTodo():
    print(" Ciudades para graficar")
    print("")
    if ciudades.largo  == 0:
        print("No hay Ciudades ingresados")
    else:
        print("Ciudades Disponibles")
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
    with open("Salida/" + nombreCiudad + ".txt") as archivo:
        l = 0
        c = 0
        lineas = archivo.readlines()
        for linea in lineas:
            columnas = linea
            l += 1
            for col in columnas:
                if col != '\n':
                    c += 1
                    matriz.insert(l, c, col)
            c = 0
            matriz.graficarNeato(nombreCiudad)
            nuevonombre = "matriz_"+nombreCiudad
    webbrowser.open("Grafico/" + nuevonombre + ".pdf")


def menu():
    opcion = ''
    while opcion != '5':
        print("------Menu principal------")
        print("1. Cargar archivo")
        print("2. Procesar archivo")
        print("3. Escribir archivo de salida")
        print("4. Generar grafica")
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
            print("")
        elif opcion != "5":
            print("Ingrese una opcion correcta" +"\n" )
        else:
            print("Gracias por usar nuestro programa :D")
            break

menu()      