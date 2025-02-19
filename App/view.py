﻿"""
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

#from DISClib.DataStructures.arraylist import getElement
from os import name
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
                  art["ConstituentID"] + ', Fecha : ' + art['DateAcquired'] + ', Medio : ' + art['Medium']
                  + ', Dimensiones: ' + art["Dimensions"])
    else:
       print('No se encontraron obras')


def printgetartistname(obras):
   size = lt.size(obras)
   nw = lt.newList()
   if size:
       print("Número total de obras del artista: " + str(size))
       tecnicas = controller.tecnicasporautor(obras)
       print("Número total de tecnicas del artista: " + str(lt.size(tecnicas)))
       conteo = controller.contartecnicas(obras, tecnicas)
       mayor = controller.mayor(conteo)
       present = lt.isPresent(conteo, mayor)
       mtec = lt.getElement(tecnicas, present)
       print("La técnica más usada por el artista es: " + str(mtec))
       i = 1
       while i <= size:
            x = lt.getElement(obras, i)
            if x["Medium"] == mtec:
                lt.addLast(nw, x)
            i += 1
       for art in lt.iterator(nw):
            print('Título: ' + art['Title'] + ',  Fecha de la obra: ' +
                art['Date'] + ', Medio: ' + art['Medium'] + ', Dimensiones: ' + art['Dimensions'])
   else:
       print('No se encontraron artistas')


def printgetcosbydepartment(catalog, obras):
    size = lt.size(obras)
    nw = lt.newList()
    nc = lt.newList()
    if size:
       print("Número total de obras a tranportar: " + str(size))
       areas = controller.areadeunaobra(obras)
       costos = controller.precioobras(areas, obras)
       obras = controller.anadirprecio(obras, costos)
       costototal = round(controller.preciototal(costos), 3)
       peso = controller.pesototal(obras)
       print("El peso total de las obras (kg) de la carga es: " + str(peso))
       print("El precio estimado (USD) de la carga es: " + str(costototal))
       orden = controller.sortdates(obras)
       i = 1
       while i <= 5:
            x = lt.getElement(orden, i)
            lt.addLast(nw, x)
            i += 1
       for num in range(1, lt.size(nw)):
           x = lt.getElement(nw, num)
           id = x["ConstituentID"]
           pos = id.strip('[]')
           h = lt.isPresent(catalog["ids"], pos)
           x["ConstituentID"] = lt.getElement(catalog["names"], h)
       print("/Las 5 obras más antiguas a transportar son: ")
       for art in lt.iterator(nw):
            print('Título: ' + str(art['Title']) + ',  Artista(s): ' +
                art['ConstituentID'] + ', Clasificación: ' + art['Classification'] + ', Fecha de la obra: ' + art['Date'] +
                ', Medio: ' + art["Medium"] + ', Dimensiones: ' + art["Dimensions"] + ', Costo de transporte: ' + str(art["precios"]))
       obras = controller.sorprecio(obras)
       i = 1
       while i <= 5:
            x = lt.getElement(obras, i)
            lt.addLast(nc, x)
            i += 1
       print("Las 5 obras más costosas de transportar: ")
       for art in lt.iterator(nc):
            print('Título: ' + str(art['Title']) + ',  Artista(s): ' +
                art['ConstituentID'] + ', Clasificación: ' + art['Classification'] + ', Fecha de la obra: ' + art['Date'] +
                ', Medio: ' + art["Medium"] + ', Dimensiones: ' + art["Dimensions"] + ', Costo de transporte: ' + str(round(art["precios"], 3)))

    else:
        print('No se encontraron obras')




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
        print('nombres cargados: ' + str(lt.size(catalog['names'])))
        print('ids cargados: ' + str(lt.size(catalog['ids'])))
        print("Departamentos cargados: " + str(lt.size(catalog['departamentos'])))
        print("IDS de objectos cargados: " + str(lt.size(catalog['objectid'])))
    elif int(inputs[0]) == 2:
        inc = int(input("Ingrese el año inicial de búsqueda: "))
        fin = int(input("Ingrese el año final de búsqueda: "))
        artits = controller.getartistcron(catalog, inc, fin)
        printartcron(artits)
    elif int(inputs[0]) == 3:
        finc = str(input("Ingrese la fecha incial de búsqueda (AAAA-MM-DD): "))
        ffin = str(input("Ingrese la fecha final de búsqueda (AAAA-MM-DD): "))
        finc = strptime(finc, "%Y-%m-%d")
        ffin = strptime(ffin, "%Y-%m-%d")
        artworks = controller.getartworkcron(catalog, finc, ffin)
        printartworkcron(artworks)
    elif int(inputs[0]) == 4:
        nombre = str(input("Ingrese el nombre del artista a consultar: "))
        obras = controller.getartistname(catalog, nombre)
        printgetartistname(obras)
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        departamento = str(input("Ingrese el departamento a consultar: "))
        obras = controller.getcosbydepartment(catalog, departamento)
        printgetcosbydepartment(catalog, obras)
    else:
        sys.exit(0)
sys.exit(0)
