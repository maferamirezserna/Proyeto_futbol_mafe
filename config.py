# Importar librerias utilizadas para el proceso
from gestion import *

# Variables globales
global equipos, jugadores, partidos, arbitros
# Cargar datos desde los archivos json.
equipos = cargar_datos("data/equipos.json")
jugadores = cargar_datos("data/jugadores.json")
partidos = cargar_datos("data/partidos.json")
arbitros = cargar_datos("data/arbitros.json")
