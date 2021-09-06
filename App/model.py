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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'artworks': None,
               'artists': None
               }

    catalog['artworks'] = lt.newList()
    catalog['artists'] = lt.newList()
    return catalog


# Funciones para agregar informacion al catalogo

def addartwork(catalog, artworks):
    # Se adiciona el artwork a la lista de artworks
    lt.addLast(catalog['artworks'], artworks)
    # Se obtienen los ids del artwork
    ids = artworks['ConstituentID'].split(",")
    # lista de ids
    for artwork in ids:
        lt.addLast(catalog['artworks'], ids)


def addartist(catalog, artists):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    lt.addLast(catalog['artists'], artists)
    ids = artists['ConstituentID'].split(",")
    for artist in ids:
        lt.addLast(catalog['artists'], ids)


# Funciones para creacion de datos


def newIDS(id):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """



# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def compareauthors(authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1

def comparetagnames(name, tag):
    return (name == tag['name'])

# Funciones de ordenamiento