# Llamo al archivo .py que contiene las variables globales que cargo para uso general
from config import equipos, jugadores, arbitros

# Funcion para visualizar la información de la tabla de las posiciones
def generar_tabla_posiciones():
    """
    Genera y muestra la tabla de posiciones de los equipos.

    La tabla de posiciones se ordena en función de los puntos acumulados por cada equipo.
    Se imprime la posición, nombre del equipo, puntos totales, y estadísticas de partidos jugados,
    ganados, empatados y perdidos, así como goles a favor y en contra.

    Retorno de datos:
        None: La función imprime directamente la tabla de posiciones en la consola.
    """
    # Ordenar por la cantidad de puntos ganados en orden descendente
    # Lambda 
    posiciones_ordenados = sorted(equipos, key=lambda x: x["estadisticas"]["puntos"], reverse=True)
    print("\nTabla de posiciones:")
    for idx, equipo in enumerate(posiciones_ordenados, start=1):
        estadisticas = equipo['estadisticas']
        print(f"{idx}. {equipo['nombre']} - {estadisticas['puntos']} pts | "
                f"{estadisticas['ganados']}G-{estadisticas['empatados']}E-{estadisticas['perdidos']}P | "
                f"GF: {estadisticas['goles_favor']} GC: {estadisticas['goles_contra']}")

# Función para visualizar tabla dee goleadores
def generar_lista_goleadores(top_n):
    """
    Genera y muestra la lista de goleadores de la competición, limitada a la cantidad especificada.

    La lista se ordena en función de la cantidad de goles anotados por cada jugador.
    Se imprime el nombre del jugador junto con la cantidad total de goles.

    Argumentos de entrada:
        top_n (int): La cantidad de goleadores a mostrar, en orden descendente de goles.

    Retorno de datos:
        None: La función imprime directamente la lista de goleadores en la consola.
    """
    # Ordenar por la cantidad de goles realizados en orden descendente
    goleadores_ordenados = sorted(jugadores, key=lambda j: j["estadisticas"]["goles"], reverse=True)
    
    # Limitar la lista a los primeros 'top_n' goleadores
    top_goleadores = goleadores_ordenados[:top_n]

    print(f"\nLista de los {top_n} mejores goleadores:")
    for jugador in top_goleadores:
        print(f"{jugador['nombre']} - {jugador['estadisticas']['goles']} goles")

# Función para visualizar reporte de árbitros
def generar_reporte_arbitros():
    """
    Genera y muestra un reporte de árbitros que han dirigido partidos.

    El reporte se ordena en función de la cantidad de partidos dirigidos por cada árbitro.
    Se imprime el nombre del árbitro, el número de partidos dirigidos, la experiencia en años
    y la categoría del árbitro.

    Retorno de datos:
        None: La función imprime directamente el reporte de árbitros en la consola.
    """
    # Ordenar por la cantidad de partidos dirigidos en orden descendente
    arbitros_ordenados = sorted(arbitros, key=lambda a: a['partidos_dirigidos'], reverse=True)
    print("\nReporte de Árbitros:")
    for arbitro in arbitros_ordenados:
        print(f"{arbitro['nombre']} - {arbitro['partidos_dirigidos']} partidos dirigidos "
                f"(Experiencia: {arbitro['experiencia']} años, Categoría: {arbitro['categoria']})")

# Función para visualizar reporte de estadísticas de equipo
def generar_estadisticas_equipo():
    """
    Muestra un reporte de todos los datos de los equipos en la lista.

    Argumento de entrada:
        equipos (list): Lista de diccionarios con la información de cada equipo.
    """
    if not equipos:
        print("No hay equipos para mostrar en el reporte.")
        return

    print("\n--- Reporte de Equipos ---\n")
    for equipo in equipos:
        print(f"ID: {equipo['id']}")
        print(f"Nombre: {equipo['nombre']}")
        print(f"Ciudad: {equipo['ciudad']}")
        print(f"Director Técnico: {equipo['director_tecnico']}")
        print("Estadísticas:")
        print(f"  - Puntos: {equipo['estadisticas']['puntos']}")
        print(f"  - Jugados: {equipo['estadisticas']['jugados']}")
        print(f"  - Ganados: {equipo['estadisticas']['ganados']}")
        print(f"  - Empatados: {equipo['estadisticas']['empatados']}")
        print(f"  - Perdidos: {equipo['estadisticas']['perdidos']}")
        print(f"  - Goles a Favor: {equipo['estadisticas']['goles_favor']}")
        print(f"  - Goles en Contra: {equipo['estadisticas']['goles_contra']}")
        print("-" * 30)  # Separador entre equipos
    print("\n--- Fin del Reporte ---\n")
