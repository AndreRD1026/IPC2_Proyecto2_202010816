import xml.etree.ElementTree as ET
from listaSimpleCiudad import ListaSimple as listaciudad
import graphviz
import time

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
                if elemento.tag == "ciudad": 
                    nombre = elemento.attrib['filas']
                    buscarCiudad = ciudades.buscarCiudad(nombre)
                    if buscarCiudad is None:
                        filas = str(elemento.find('nombre').text)             
                        ciudades.agregar(nombre,filas)   

            print("")
            ciudades.mostrarElementos()
            #print("ciudades Ingresados: ")

        
            
            time.sleep(0.5)
        except:
            print("")
            print("¡¡ ERROR !!")
            print("El archivo proporcionado no cumple con los estándares de las ciudades")

    else:
        print("¡¡ ERROR !!")
        print("El archivo cargado no es compatible con un .xml")


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
            #Filename = input('Ingrese la ruta del archivo: ')
            #file = Filename
            cargarArchivo()
        elif opcion == '2':
            #procesararchivo()
            print("")
        elif opcion == '3':
            print("Archivo de salida" +"\n" )
        elif opcion == '4':
            #graficoarchivo()
            #grafica2()
            print("")
        elif opcion != "5":
            print("Ingrese una opcion correcta" +"\n" )
        else:
            print("Gracias por usar nuestro programa :D")
            break

menu()      