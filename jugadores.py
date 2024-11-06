# Importar librerias utilizadas para el proceso
import json
# Llamo al archivo .py que contiene las variables globales que cargo para uso general
from config import jugadores

# Verificar si el ID del jugador ya existe
def jugador_existe(id_jugador):
    """
    Verifica si un jugador con el ID dado ya existe en la lista de jugadores.

    Argumento de entrada:
        id_jugador (int): El ID del jugador a verificar.

    Retorno de datos:
        bool: Retorna True si el jugador existe, False en caso contrario.
    """
    return any(jugador["id"] == id_jugador for jugador in jugadores)

# función para agregar un jugador
def registrar_jugador(id_jugador, nombre, numero, posicion, equipo_id):
    """
    Registra un nuevo jugador y lo guarda en la lista de jugadores si no existe.

    Argumentos de entrada:
        id_jugador (int): ID del jugador a registrar.
        nombre (str): Nombre del jugador.
        numero (int): Número de camiseta del jugador.
        posicion (str): Posición del jugador en el campo.
        equipo_id (int): ID del equipo al que pertenece el jugador.

    Retorno de datos:
        list: Devuelve la lista de jugadores actualizada, o None si ya existe un jugador con el mismo ID.
    """

    if not any(equipo["equipo_id"] == equipo_id for equipo in equipos):
        print(f"Error: El equipo con ID {equipo_id} no existe. No se puede registrar el jugador.")
        return None

    if jugador_existe(id_jugador):
        print(f"Error: Ya existe un jugador con el ID {id_jugador}.")
        return None

    jugador = {
        "id": id_jugador,
        "nombre": nombre,
        "numero": numero,
        "posicion": posicion,
        "equipo_id": equipo_id,
        "estadisticas": {
            "partidos": 0,
            "goles": 0,
            "asistencias": 0,
            "amarillas": 0,
            "rojas": 0,
            "minutos": 0
        }
    }
    jugadores.append(jugador)
    print(f"Jugador '{nombre}' registrado con éxito.")
    return jugadores

# Cargar jugadores desde el archivo jugadores.json al iniciar el programa
def cargar_jugadores():
    """
    Carga la lista de jugadores desde el archivo 'jugadores.json'.
    Si el archivo no existe, inicializa una lista vacía de jugadores.

    Retorno de datos:
        None: La función actualiza la lista de jugadores globalmente.
    """
    try:
        with open("jugadores.json", "r") as archivo:
            global jugadores
            jugadores = json.load(archivo)
    except FileNotFoundError:
        jugadores = []  # Si no existe el archivo, inicializa una lista vacía

# Función para buscar un jugador
def buscar_jugador(criterio, valor):
    """
    Busca todos los jugadores que cumplan con un criterio específico y un valor, y devuelve su información.
    Si no existe ningún jugador que cumpla con el criterio, devuelve una lista vacía.

    Argumentos de entrada:
        criterio (str): El criterio de búsqueda (ej. "nombre", "posición").
        valor (str): El valor a buscar para el criterio especificado (ej. "Delantero").

    Retorno de datos:
        list: Una lista de diccionarios con la información de los jugadores que cumplen con el criterio.
    """
    # ciclo de una linea para poder realizar la busquedar en los diferentes jugadores almacenados.
    return [jugador for jugador in jugadores if str(jugador.get(criterio, "")).lower() == str(valor).lower()]

# Función para buscar el equipo 
def buscar_jugador2(id_jugador):
    """
    Busca un equipo por su ID y devuelve su información si existe.
    Argumentos de entrada:
        id_equipo (str): El ID del jugador a registrar.

    Retorno de datos:
        Diccionario: Jugador almacenado en el JSON.
    """
    return next((e for e in jugadores if e["id"] == id_jugador), None)                                                 

# Función para verificar las posiciones
def verificar_posicion():
    """
    Se solicita ingresar una posición válida para un jugador y verifica que sea una de las opciones permitidas.
    Si el dato ingresado no es válido, solicita nuevamente al usuario la posición.

    Retorno de datos:
        str: Una cadena de texto con la posición válida (Delantero, Mediocampista, Defensa o Portero).
    """
    posiciones_validas = ["Delantero", "Mediocampista", "Defensa", "Portero"]
    
    while True:
        posicion = input("Ingresa la posición del jugador (Delantero, Mediocampista, Defensa, Portero): ").title().strip()
        if posicion in posiciones_validas:
            return posicion
        else:
            print("Error: Posición no válida. Ingresa una de las siguientes: Delantero, Mediocampista, Defensa o Portero.")

# función para actualizar estadísticas de un jugador
def actualizar_estadisticas_jugador(jugador, goles, asistencias, amarillas, rojas, minutos):
    """
    Actualiza las estadísticas de un jugador, incrementando los valores de sus
    partidos jugados, goles, asistencias, tarjetas amarillas, tarjetas rojas y minutos jugados.

    Argumentos de entrada:
        jugador (dict): Diccionario que contiene la información del jugador.
        goles (int): Número de goles anotados por el jugador en el partido.
        asistencias (int): Número de asistencias realizadas por el jugador en el partido.
        amarillas (int): Número de tarjetas amarillas recibidas por el jugador.
        rojas (int): Número de tarjetas rojas recibidas por el jugador.
        minutos (int): Minutos jugados por el jugador en el partido.

    Retorno de datos:
        None: La función actualiza la información del jugador directamente.

    Lanza:
        ValueError: Si el jugador no se encuentra.
    """
    if jugador:
        jugador["estadisticas"]["partidos"] += 1
        jugador["estadisticas"]["goles"] += goles
        jugador["estadisticas"]["asistencias"] += asistencias
        jugador["estadisticas"]["amarillas"] += amarillas
        jugador["estadisticas"]["rojas"] += rojas
        jugador["estadisticas"]["minutos"] += minutos
    else:
        raise ValueError("Jugador no encontrado.")
