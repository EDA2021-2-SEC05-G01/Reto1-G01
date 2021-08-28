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
    catalog = {'Constituent_ID': None,
               'Display_Name': None,
               'Artist_Bio': None,
               'Nationality': None,
               'Gender': None,
               'Begin_Date': None,
               'End_Date': None}

    catalog['Constituent_ID'] = lt.newList()
    catalog['Display_Name'] = lt.newList()
    catalog['Artist_Bio'] = lt.newList('ARRAY_LIST')
    catalog['Nationality'] = lt.newList()
    catalog['Gender'] = lt.newList()
    catalog['Begin_Date'] = lt.newList()
    catalog['End_Date'] = lt.newList()
    return catalog
# Funciones para agregar informacion al catalogo

def addObra(catalog, Display_Name):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['Display_Name'], Display_Name)
    # Se obtienen los autores del libro
    IDS = Display_Name['Constituent_ID'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for author in IDS:
        addIDobra(catalog, author.strip(), Display_Name)


def addIDobra(catalog, ID, obra):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    IDS = catalog['Constituent_ID']
    posID = lt.isPresent(IDS, ID)
    if posID > 0:
        ids = lt.getElement(IDS, posID)
    else:
        ids = newIDS(ID)
        lt.addLast(IDS, ids)
    lt.addLast(ids['Display_Name'], obra)


def addTag(catalog, tag):
    """
    Adiciona un tag a la lista de tags
    """
    t = newTag(tag['tag_name'], tag['tag_id'])
    lt.addLast(catalog['tags'], t)

# Funciones para creacion de datos


def newIDS(id):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    ids = {'Constituent_ID': "", "Display_Name": None,  "average_rating": 0}
    ids['Constituent_ID'] = id
    ids['Display_Name'] = lt.newList('ARRAY_LIST')
    return ids


def newTag(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    tag = {'name': '', 'tag_id': ''}
    tag['name'] = name
    tag['tag_id'] = id
    return tag


def newBookTag(tag_id, book_id):
    """
    Esta estructura crea una relación entre un tag y
    los libros que han sido marcados con dicho tag.
    """
    booktag = {'tag_id': tag_id, 'book_id': book_id}
    return booktag


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def compareauthors(authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1

def comparetagnames(name, tag):
    return (name == tag['name'])

# Funciones de ordenamiento