"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from time import strptime
import config as cf
import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*1000)
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las obras")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Calcular costo de tranporte de un departamento")
    print("0 - Salir de la aplicación")

def initCatalog(opcion):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(opcion)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def printartcron(artists):
   size = lt.size(artists)
   if size:
       print("Número total de artistas en el rango: " + str(size))
       i = 1
       nw = lt.newList()
       while i <= 3:
           lt.addLast(nw, lt.getElement(artists, i))
           i += 1
       i = size - 2
       while i <= size:
           lt.addLast(nw, lt.getElement(artists, i))
           i += 1
       for art in lt.iterator(nw):
           print('Nombre: ' + art['DisplayName'] + ',  Año Nacimiento: ' +
                  art['BeginDate'] + ', Nacionalidad: ' + art['Nationality'] + ', Género: ' + art['Gender'])
   else:
       print('No se encontraron artistas')

def printartworkcron(artworks):
    size = lt.size(artworks)
    if size:
       print("El museo MoMa adquirió : " + str(size) + " durante este rango de fechas.")
       i = 1
       nw = lt.newList()
       while i <= 3:
           lt.addLast(nw, lt.getElement(artworks, i))
           i += 1
       i = size - 2
       pur = 0
       while i <= size:
           lt.addLast(nw, lt.getElement(artworks, i))
           i += 1
       for art in lt.iterator(nw):
           if art["CreditLine"] == "Purchase":
               pur +=1
       print("Total de obras adquiridas a través de compra: " + str(pur))
    #    artistas = controller.getartistID(catalog, nw)
       for art in lt.iterator(nw):
           print('Titulo: ' + art['Title'] + ',  Artistas : ' +
                  art['ConstituentID'] + ', Fecha : ' + art['DateAcquired'] + ', Medio : ' + art['Medium']
                  + ', Dimensiones: ' + art["Dimensions"])
    else:
       print('No se encontraron obras')

def printSortResults(ord_books, sample=10):
    size = lt.size(ord_books)
    if size > sample:
        print("Los primeros ", sample, " libros ordenados son:")
    i=1
    while i <= sample:
        book = lt.getElement(ord_books,i)
        print('Titulo: ' + book['Title'])
        i+=1


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        print("Escoja el tipo de representación de lista que desea utilizar:")
        print("1. ARRAY_LIST")
        print("2. LINKED_LIST")
        opcion = input("Su opción: ")
        catalog = initCatalog(opcion)
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
    elif int(inputs[0]) == 2:
        inc = int(input("Ingrese el año inicial de búsqueda: "))
        fin = int(input("Ingrese el año final de búsqueda: "))
        artits = controller.getartistcron(catalog, inc, fin)
        print(printartcron(artits))
    elif int(inputs[0]) == 3:
        finc = str(input("Ingrese la fecha incial de búsqueda (AAAA-MM-DD): "))
        ffin = str(input("Ingrese la fecha final de búsqueda (AAAA-MM-DD): "))
        finc = strptime(finc, "%Y-%m-%d")
        ffin = strptime(ffin, "%Y-%m-%d")
        artworks = controller.getartworkcron(catalog, finc, ffin)
        print(printartworkcron(artworks))
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        pass
    elif int(inputs[0]) == 7:
        pass
    else:
        sys.exit(0)
sys.exit(0)
