"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from os import curdir
from time import strptime
from time import process_time
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Algorithms.Sorting import quicksort as qck
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(opcion):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'artworks': None,
               'artists': None
               }
    if opcion == "1":
        opcion = "ARRAY_LIST"
    elif opcion == "2":
        opcion = "LINKED_LIST"
    catalog['artworks'] = lt.newList(opcion)
    catalog['artists'] = lt.newList(opcion)
    return catalog


# Funciones para agregar informacion al catalogo

def addartwork(catalog, artworks):
    # Se adiciona el artwork a la lista de artworks
    lt.addLast(catalog['artworks'], artworks)
    # Se obtienen los ids del artwork
    ids = artworks['ConstituentID'].split(",")


def addartist(catalog, artists):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    lt.addLast(catalog['artists'], artists)
    ids = artists['ConstituentID'].split(",")


# Funciones para creacion de datos


def newIDS(id):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """



# Funciones de consulta

def getartistcron(catalog, inc, fin):
    """
    Retorna los mejores libros
    """
    cron = lt.newList()
    artists = catalog['artists']
    for num in range(1, lt.size(artists)):
        m = num
        x = lt.getElement(catalog['artists'], m)
        nacimiento = x["BeginDate"]
        nacimiento = int(nacimiento)
        if nacimiento >= inc and nacimiento <= fin:
            lt.addLast(cron, x)
    sortartist(cron)
    return cron

def getartworkcron(catalog, finc, ffin):
    """
    Retorna los mejores libros
    """
    cron = lt.newList()
    artworks = catalog['artworks']
    for num in range(1, lt.size(artworks)):
        m = num
        x = lt.getElement(catalog['artworks'], m)
        fecha = x["DateAcquired"]
        if fecha != '':
            fecha = strptime(fecha, "%Y-%m-%d")
            if fecha >= finc and fecha <= ffin:
                lt.addLast(cron, x)
    sortfechas(cron)
    return cron

# def getartistID(catalog, nw):
#     for x in lt.iterator(nw):

#     return None



# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtworkByDateAcquired(finc, ffin):
    finc = finc['DateAcquired']
    ffin = ffin['DateAcquired']
    if finc != '' and ffin != '':
        finc = strptime(finc, "%Y-%m-%d")
        ffin = strptime(ffin, "%Y-%m-%d")
    return finc < ffin

def compareBeginDate(art1, art2):
    return float(art1['BeginDate']) < float(art2['BeginDate'])


# Funciones de ordenamiento

def sortartist(catalog):
    sa.sort(catalog, compareBeginDate)

def sortfechas(catalog):
    sa.sort(catalog, cmpArtworkByDateAcquired)

def sortDates(catalog, size, typesort):
    # TODO completar modificaciones para el laboratorio 4
    if typesort == "1":
        typesort = ins
    elif typesort == "2":
        typesort = sa
    elif typesort == "3":
        typesort = mg
    elif typesort == "4":
        typesort = qck
    sub_list = lt.subList(catalog['artworks'], 1, size)
    sub_list = sub_list.copy()
    start_time = process_time()
    sorted_list = typesort.sort(sub_list, cmpArtworkByDateAcquired)
    stop_time = process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list