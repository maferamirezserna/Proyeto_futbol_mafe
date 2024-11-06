# importamos las funciones correspondientes a partidos
from config import partidos

# Función para verificar si exite el partido
def verificar_partido(id_partido):
    """
    Verifica si un partido con el ID dado ya existe.
    Argumento de entrada:
        id_partido (int): El ID del partido a verificar.

    Retorno de datos:
        bool: True si el partido existe, False en caso contrario.
    """
    for partido in partidos:
        if partido["id"] == id_partido:
            return True
    return False

# Función para verificar que no exista un partido con la misma fecha y nombre de equipos
def existe_partido_entre_equipos(fecha, equipo_local, equipo_visitante):
    """Verifica si ya existe un partido entre los mismos equipos en la misma fecha.
    Argumentos de entrada:
        fecha (str): La fecha del partido a verificar en formato YYYY-MM-DD.
        equipo_local (str): Nombre del equipo local.
        equipo_visitante (str): Nombre del equipo visitante.

    Retorno de datos:
        bool: True si ya existe un partido entre los mismos equipos en la misma fecha, False en caso contrario.
    """
    for partido in partidos:
        if (partido['fecha'] == fecha and 
            ((partido['equipo_local'] == equipo_local and partido['equipo_visitante'] == equipo_visitante) or
             (partido['equipo_local'] == equipo_visitante and partido['equipo_visitante'] == equipo_local))):
            return True
    return False

# Función para agregar el alineamiento del equipo
def agregar_alineacion(id_partido):
    """
    Agrega la alineación local y visitante a un partido específico.

    Argumento de entrada:
        id_partido (str): ID del partido al que se asignará la alineación.

    Retorno de datos:
        None: Imprime el resultado de la asignación.
    """
    # Buscar el partido por ID
    partido = next((p for p in partidos if p["id"] == id_partido), None)
    if partido is None:
        print("Error: El ID del partido no existe.")
        return

    # Agregar alineación del equipo local
    alineacion_local = input("Ingrese la alineación del equipo local (separados por comas): ")
    alineacion_local = [jugador.strip() for jugador in alineacion_local.split(",") if jugador.strip()]
    
    if not alineacion_local:
        print("Error: La alineación local no puede estar vacía.")
        return

    partido["alineacion_local"] = alineacion_local

    # Agregar alineación del equipo visitante
    alineacion_visitante = input("Ingrese la alineación del equipo visitante (separados por comas): ")
    alineacion_visitante = [jugador.strip() for jugador in alineacion_visitante.split(",") if jugador.strip()]
    
    if not alineacion_visitante:
        print("Error: La alineación visitante no puede estar vacía.")
        return

    partido["alineacion_visitante"] = alineacion_visitante

    print(f"Alineaciones agregadas exitosamente al partido {id_partido}.")
    print(f"Alineación local: {partido['alineacion_local']}")
    print(f"Alineación visitante: {partido['alineacion_visitante']}")

# Función para agregar un partido
def registrar_partido(id_partido, fecha, id_arbitro, equipo_local, equipo_visitante):
    """Registra un nuevo partido y lo guarda en la lista.
    Argumento de entrada:
        id_partido (str): El ID único del partido a registrar.
        fecha (str): La fecha del partido en formato YYYY-MM-DD.
        id_arbitro (int): El ID del árbitro asignado al partido.
        equipo_local (str): Nombre del equipo que juega en casa.
        equipo_visitante (str): Nombre del equipo que juega como visitante.

    Retorno de datos:
        list: La lista de partidos actualizada si el registro fue exitoso; None en caso de error.
    """
    if verificar_partido(id_partido):
        print(f"Error: Ya existe un equipo con el ID {id_partido}.")
        return None

    if existe_partido_entre_equipos(fecha, equipo_local, equipo_visitante):
        print(f"Error: Ya existe un partido entre {equipo_local} y {equipo_visitante} en la fecha {fecha}.")
        return None

    partido = {
        "id": id_partido,
        "fecha": fecha,
        "arbitro_id": id_arbitro,
        "equipo_local": equipo_local,
        "equipo_visitante": equipo_visitante,
        "goles_local": 0,
        "goles_visitante": 0,
        "alineamiento_local":[],
        "alineamiento_visitante":[],
        "eventos": []
    }
    partidos.append(partido)
    print(f"Partido registrado entre {equipo_local} y {equipo_visitante}.")
    return partidos

# Función para buscar un partido
def buscar_partido(id_partido):
    """Busca un partido por su ID y muestra su información.
    Si no existe, muestra un mensaje de error.

    Argumento de entrada:
        id_partido (int): El ID del partido a verificar.

    Retorno de datos:
        dict: Imprime la información del partido si existe; None en caso de error.
    """
    for partido in partidos:
        if partido["id"] == id_partido:
            print("\n--- Información del Partido ---")
            print(f"ID: {partido['id']}")
            print(f"Fecha: {partido['fecha']}")
            print(f"Árbitro ID: {partido['arbitro_id']}")
            print(f"Equipo Local: {partido['equipo_local']}")
            print(f"Equipo Visitante: {partido['equipo_visitante']}")
            print(f"Goles Local: {partido['goles_local']}")
            print(f"Goles Visitante: {partido['goles_visitante']}")
            print('Eventos: \n')
            print(f"Equipo: {partido['eventos']['equipo']}")
            print(f"Tipo: {partido['eventos']['tipo']}")
            print(f"Minuto: {partido['eventos']['minuto']}")
            print(f"Jugador: {partido['eventos']['jugador']}")
            return
    print(f"No se encontró ningún partido con ID: {id_partido}.")

# función para actualizar resultados del artido
def actualizar_resultados(id_partido, goles_local, goles_visitante):
    """Actualiza los resultados de un partido.
    
    Argumentos de entrada:
        id_partido (int): El ID del partido cuyo resultado se desea actualizar.
        goles_local (int): La cantidad de goles anotados por el equipo local.
        goles_visitante (int): La cantidad de goles anotados por el equipo visitante.

    Retorno de datos:
        None: Imprime un mensaje confirmando que los resultados se han actualizado, o un mensaje de error si no se encuentra el partido.
    """
    for partido in partidos:
        if partido["id"] == id_partido:
            partido["goles_local"] = goles_local
            partido["goles_visitante"] = goles_visitante
            print("Resultados actualizados.")
            return
    print(f"No se encontró ningún partido con ID: {id_partido}.")

# función para colocar el evento sucedido
def registrar_evento(id_partido, minuto, tipo_evento, jugador, equipo):
    """Registra un evento en un partido.
    Argumentos de entrada:
        id_partido (int): El ID del partido en el que ocurrió el evento.
        minuto (int): El minuto del partido en el que ocurrió el evento.
        tipo_evento (str): El tipo de evento (por ejemplo, "gol", "tarjeta", "sustitución").
        jugador (str): El nombre del jugador involucrado en el evento.
        equipo (str): El nombre del equipo al que pertenece el jugador.

    Retorno de datos:
        None: Agrega el evento al partido correspondiente y no retorna ningún valor explícito.
    """
    for partido in partidos:
        if partido["id"] == id_partido:
            evento = {
                "minuto": minuto,
                "tipo": tipo_evento,
                "jugador": jugador,
                "equipo": equipo
            }
            partido["eventos"].append(evento)
            print(f"Evento registrado en el minuto {minuto}.")
            return
    print(f"No se encontró ningún partido con ID: {id_partido}.")