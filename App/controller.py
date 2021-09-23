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
 """
from DISClib.ADT import list as lt
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog(opcion):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(opcion)
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtworks(catalog)
    loadArtists(catalog)
    loadnames(catalog)
    loadids(catalog)
    loaddep(catalog)
    loadobj(catalog)


def loadArtworks(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    Artfile = cf.data_dir + 'Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(Artfile, encoding='utf-8'))
    for artista in input_file:
        model.addartwork(catalog, artista)


def loadArtists(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    Artistsfile = cf.data_dir + 'Artists-utf8-large.csv'
    input_file = csv.DictReader(open(Artistsfile, encoding='utf-8'))
    for artista in input_file:
        model.addartist(catalog, artista)

def loadnames(catalog):
    for x in lt.iterator(catalog['artists']):
        lt.addLast(catalog['names'], x['DisplayName'])

def loadids(catalog):
    for x in lt.iterator(catalog['artists']):
        lt.addLast(catalog['ids'], x['ConstituentID'])

def loaddep(catalog):
    for x in lt.iterator(catalog['artworks']):
        lt.addLast(catalog['departamentos'], x['Department'])

def loadobj(catalog):
    for x in lt.iterator(catalog['artworks']):
        lt.addLast(catalog['objectid'], x['ObjectID'])



# Funciones de ordenamiento

def sortBeginDate(catalog):
    """
    Ordena los libros por average_rating
    """
    model.sortartist(catalog)

def sortDates(catalog, size, typesort):
    """
    Ordena los libros por average_rating
    """
    return model.sortDates(catalog, size, typesort)


# Funciones de consulta sobre el catálogo

def getartistcron(catalog, inc, fin):
    """
    Retorna los mejores libros
    """
    artists = model.getartistcron(catalog, inc, fin)
    return artists


def getartworkcron(catalog, finc, ffin):
    """
    Retorna los mejores libros
    """
    artists = model.getartworkcron(catalog, finc, ffin)
    return artists

def getartistname(catalog, name):
    """
    Retorna los mejores libros
    """
    artists = model.getartistname(catalog, name)
    return artists

def tecnicasporautor(obras):
    tecnicas = model.tecnicasporautor(obras)
    return tecnicas

def contartecnicas(obras, tecnicas):
    conteo = model.contartecnicas(obras, tecnicas)
    return conteo

def mayor(lista):
    mayor = model.mayor(lista)
    return mayor

def getcosbydepartment(catalog, departamento):
    costo = model.getcosbydepartment(catalog, departamento)
    return costo

def areadeunaobra(obras):
    areas = model.areadeunaobra(obras)
    return areas

def precioobras(areas, obras):
    costos = model.precioobras(areas, obras)
    return costos

def preciototal(costos):
    preciototal = model.preciototal(costos)
    return preciototal

def pesototal(obras):
    peso = model.pesototal(obras)
    return peso

def sortdates(obras):
    ob = model.sortdates(obras)
    return ob

def anadirprecio(obras, precios):
    ob = model.anadirprecio(obras, precios)
    return ob

def sorprecio(obras):
    ob = model.sorprecio(obras)
    return ob