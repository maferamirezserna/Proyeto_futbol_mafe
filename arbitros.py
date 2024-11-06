# Llamo al archivo .py que contiene las variables globales que cargo para uso general
from config import *
from gestion import *

# Función con verificación si existe el arbitro
def arbitro_existe(id_arbitro):
    """Busca un árbitro por su ID y muestra su información.
    
    Argumento de entrada:
        id_arbitro (str): El ID del árbitro a verificar.

    Retorno de datos:
        bool: Retorna True si el árbitro existe, False en caso contrario.
    """
    return any(equipo["id"] == id_arbitro for equipo in arbitros)

# Función de almacenar el registro del árbitro 
def registrar_arbitro(id_arbitro, nombre, experiencia, categoria):
    """Registra un nuevo equipo y lo guarda en equipos.json si no existe.
    Argumentos de entrada:
        id_arbitro (str): ID del árbitro a registrar.
        nombre (str): Nombre del árbitro.
        experiencia (int): Años de experiencia del árbitro.
        categoria (str): Categoría del árbitro (Fifa, Nacional, Regional).

    Retorno de datos:
        list: Devuelve la lista de árbitros actualizada, o None si ya existe un árbitro con el mismo ID.
    """
    if arbitro_existe(id_arbitro):
        print(f"Error: Ya existe un arbitro con el ID {id_arbitro}.")
        return None
    
    arbitro = {
        'id': id_arbitro,
        'nombre': nombre,
        'experiencia': experiencia,  # Años de experiencia
        'categoria': categoria,      # Categoría del árbitro
        'partidos_dirigidos': 0      # Inicialmente en 0
    }
    arbitros.append(arbitro)
    print(f"Arbitro '{nombre}' registrado con éxito.")
    return arbitros

# Función para verificar si la cateroría seleccionada 
def verificar_categoria_arbitro():
    """
    Solicita al usuario ingresar una categoría de árbitro y verifica si es válida.

    Retorno de datos:
        str: Retorna la categoría válida seleccionada por el usuario.
    """
    categorias_validas = ["Fifa", "Nacional", "Regional"]  # Lista de categorías permitidas
    while True:
        categoria = verificar_string("Ingresa la categoría del árbitro (Fifa, Nacional, Regional): ").title().strip().capitalize()
        if categoria in categorias_validas:
            return categoria  # Retorna la categoría válida
        else:
            print("Error: Categoría no válida. Ingresa 'FIFA', 'Nacional' o 'Regional'.")

# Función para buscar un arbitro específico
def buscar_arbitro(nombre_arbitro):
    """
    Busca un árbitro por su nombre y devuelve su información si existe.

    Argumento de entrada:
        id_arbitro (str): El nombre del árbitro a buscar.

    Retorno de datos:
        dict: Retorna un diccionario con la información del árbitro, o None si no se encuentra.
    """
    return next((e for e in arbitros if e["nombre"].lower() == nombre_arbitro.lower()), None)

# Función para actualizar la información relacionada con los partidos
def actualizar_partidos_arbitro(arbitro, experiencia, categoria):
    """
    Actualiza la información de partidos dirigidos por el árbitro.

    Argumentos de entrada:
        arbitro (dict): Diccionario que contiene la información del árbitro.
        experiencia (int): Años adicionales de experiencia a añadir.
        categoria (str): Nueva categoría del árbitro.

    Retorno de datos:
        None: La función actualiza la información del árbitro directamente.
    """
    if arbitro:
        arbitro['partidos_dirigidos'] += 1
        arbitro['experiencia'] += experiencia
        arbitro['categoria'] = categoria

# Función para verificar si esta disponible el árbitro para el partido en la fecha.
def verificar_arbitro_disponible(id_arbitro, fecha):
    """
    Verifica si un árbitro está disponible en una fecha específica.

    Argumentos de entrada:
        id_arbitro (str): ID del árbitro a verificar.
        fecha (str): Fecha en formato "YYYY-MM-DD".

    Retorno de datos:
        bool: True si el árbitro está disponible en esa fecha, False en caso contrario.
    """
    for partido in partidos:
        if partido["arbitro_id"] == id_arbitro and partido["fecha"] == fecha:
            return False
    return True

def Asignar_arbitro(id_partido, id_arbitro, fecha):
    """
    Asigna un árbitro a un partido específico, verificando que el árbitro esté disponible en la fecha indicada.

    Argumentos de entrada:
        id_partido (str): ID del partido al que se asignará el árbitro.
        id_arbitro (str): ID del árbitro que se asignará al partido.
        fecha (str): Fecha del partido en formato "YYYY-MM-DD".

    Retorno de datos:
        None: Imprime el resultado de la asignación.
    """
    # Buscar el partido por ID
    print()
    partido = next((p for p in partidos if p["id"] == id_partido), None)
    if partido is None:
        print("Error: El ID del partido no existe.")
        return

    arbitro = next((p for p in arbitros if p["id"] == id_arbitro), None)
    if arbitro is None:
        print("Error: El ID del árbitro no existe.")
        return

    # Verificar que el árbitro esté disponible en la fecha
    if not verificar_arbitro_disponible(id_arbitro, fecha):
        print("Error: El árbitro ya tiene asignado un partido en esta fecha.")
        return

    # Asignar el árbitro al partido si está disponible
    partido["arbitro_id"] = id_arbitro
    partido["fecha"] = fecha
    print(f"Árbitro {id_arbitro} asignado exitosamente al partido {id_partido} en la fecha {fecha}.")
