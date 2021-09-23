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


from DISClib.ADT.indexminpq import size
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
               'artists': None,
               'names': None,
               'ids': None,
               'departamentos': None,
               'objectid': None
               }
    if opcion == "1":
        opcion = "ARRAY_LIST"
    elif opcion == "2":
        opcion = "LINKED_LIST"
    catalog['artworks'] = lt.newList(opcion)
    catalog['artists'] = lt.newList(opcion)
    catalog['names'] = lt.newList()
    catalog['ids'] = lt.newList()
    catalog['departamentos'] = lt.newList()
    catalog['objectid'] = lt.newList()
    return catalog


# Funciones para agregar informacion al catalogo

def addartwork(catalog, artworks):
    # Se adiciona el artwork a la lista de artworks
    lt.addLast(catalog['artworks'], artworks)


def addartist(catalog, artists):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    lt.addLast(catalog['artists'], artists)



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
                id = x["ConstituentID"]
                pos = id.strip('[]')
                h = lt.isPresent(catalog["ids"], pos)
                x["ConstituentID"] = lt.getElement(catalog["names"], h)
                lt.addLast(cron, x)
    sortfechas(cron)
    return cron

def getartistname(catalog, name):
    obras = obrasporautor(catalog, name)
    return obras

def getcosbydepartment(catalog, departamento):
    obras = obraspordepartamento(catalog, departamento)
    return obras


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

def compareDate(art1, art2):
    if art1['Date'] != '' and art2['Date'] != '':
        return float(art1['Date']) < float(art2['Date'])

def compareprecios(art1, art2):
    return float(art1['precios']) > float(art2['precios'])


# Funciones de ordenamiento

def sorprecio(obras):
    start_time = process_time()
    x = mg.sort(obras, compareprecios)
    stop_time = process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print("timepo: " + str(elapsed_time_mseg))
    return x

def sortdates(obras):
    start_time = process_time()
    x = mg.sort(obras,compareDate)
    stop_time = process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print("timepo: " + str(elapsed_time_mseg))
    return x

def sortartist(catalog):
    start_time = process_time()
    mg.sort(catalog, compareBeginDate)
    stop_time = process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print("timepo: " + str(elapsed_time_mseg))

def sortfechas(catalog):
    start_time = process_time()
    mg.sort(catalog, cmpArtworkByDateAcquired)
    stop_time = process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print("timepo: " + str(elapsed_time_mseg))

def sortDates(catalog, size, typesort):
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

def obrasporautor(catalog, name):
    obras = lt.newList()
    posicion = lt.isPresent(catalog["names"], name)
    id = lt.getElement(catalog["ids"], posicion)
    for x in lt.iterator(catalog["artworks"]):
        if id == (x["ConstituentID"]).strip("[]"):
            lt.addLast(obras, x)
    return obras

def tecnicasporautor(obras):
    tecnicas = lt.newList()
    j = 1
    while j < size(obras):
        x = lt.getElement(obras, j)
        j += 1
        tecnica = x["Medium"]
        if lt.isPresent(tecnicas, tecnica) == 0:
            lt.addLast(tecnicas, tecnica)
    return tecnicas

def contartecnicas(obras, tecnicas):
    i = 1
    conteos = lt.newList()
    while i <= size(tecnicas):
        j = 1
        conteo = 0
        while j <= size(obras):
            medium = lt.getElement(obras, j)
            if lt.getElement(tecnicas, i) == medium["Medium"]:
                conteo += 1
            j += 1
        lt.addLast(conteos, conteo)
        i += 1
    return conteos


def mayor(lista):
    mayor = 0
    i = 1
    while i <= size(lista):
        if lt.getElement(lista, i) > mayor:
            mayor = lt.getElement(lista, i)
        i += 1
    return mayor

def obraspordepartamento(catalog, departamento):
    obras = lt.newList()
    i = 1
    artworks = catalog["artworks"]
    while i <= size(artworks):
        obra = lt.getElement(artworks, i)
        dep = obra["Department"]
        if dep == (departamento):
            lt.addLast(obras, obra)
        i += 1
    return obras


# FUNCIONES DE CÁLCULOS Y OPERACIONES

def areadeunaobra(obras):
    areas = lt.newList()
    i = 1
    while i <= size(obras):
        obra = lt.getElement(obras, i)
        if obra["Diameter (cm)"] != '':
            area = areacirculo(obra["Diameter (cm)"])
        elif obra["Depth (cm)"] != '' and obra["Depth (cm)"] != "0" and obra["Width (cm)"] != '' and obra["Width (cm)"] != "0" and obra["Height (cm)"] != '' and obra["Height (cm)"] != "0":
            area = areacubo(obra["Width (cm)"], obra["Height (cm)"], obra["Depth (cm)"])
        elif obra["Width (cm)"] != '' and obra["Width (cm)"] != "0" and obra["Height (cm)"] != '' and obra["Height (cm)"] != "0":
            area = areacuadrado(obra["Width (cm)"], obra["Height (cm)"])
        else:
            area = 0
        area = (area)
        lt.addLast(areas, area)
        i += 1
    return areas


def areacirculo(diametro):
    diam = cmam(diametro)
    area = (3.1416)*((float(diam)/2)**2)
    return area

def areacuadrado(ancho, alto):
    anc = cmam(ancho)
    alt = cmam(alto)
    area = float(anc)*float(alt)
    return area

def areacubo(ancho, alto, profundidad):
    anc = cmam(ancho)
    alt = cmam(alto)
    pro = cmam(profundidad)
    area = float(anc)*float(alt)*float(pro)
    return area

def precioobras(areas, obras):
    costos = lt.newList()
    costo = 0
    i = 1
    while i <= size(obras):
        obra = lt.getElement(obras, i)
        area = lt.getElement(areas, i)
        if obra["Weight (kg)"] != '':
            costo = float(area) + float(obra["Weight (kg)"])
        else:
            costo = float(area)
        if float(area) == 0:
            costo = 48
        else:
            costo = 72*costo
        lt.addLast(costos, costo)
        i += 1
    return costos

def preciototal(costos):
    costototal = 0
    i = 1
    while i <= size(costos):
        costo = lt.getElement(costos, i)
        costototal += float(costo)
        i += 1
    return costototal

def cmam(numero):
    numero = float(numero)
    m = numero/100
    return m

def pesototal(obras):
    i = 1
    peso = 0
    while i <= size(obras):
        obra = lt.getElement(obras, i)
        if obra["Weight (kg)"] != '':
            peso += float(obra["Weight (kg)"])
        i += 1
    return peso

def anadirprecio(obras, precios):
    i = 1
    while i <= size(obras):
        x = lt.getElement(obras, i)
        p = lt.getElement(precios, i)
        x["precios"] = p
        i += 1
    return obras