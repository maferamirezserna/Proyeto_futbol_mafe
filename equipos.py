# importamos las funciones relacionadas en gestión y variables globales
from gestion import *
# Llamo al archivo .py que contiene las variables globales que cargo para uso general
from config import equipos

# Verificar si el ID del equipo ya existe
def equipo_existe(id_equipo):
    """Verifica si un equipo con el ID dado ya existe.
    
    Argumento de entrada:
        id_equipo (int): El ID del equipo a verificar.

    Retorno de datos:
        bool: True si el equipo existe, False en caso contrario.
    """
    return any(equipo["id"] == id_equipo for equipo in equipos)

# Agregar un nuevo equipo
def registrar_equipo(id_equipo, nombre, ciudad, director_tecnico):
    """Registra un nuevo equipo y lo guarda en equipos.json si no existe.
    Argumentos de entrada:
        id_equipo (str): El ID del equipo a registrar.
        nombre (str): El nombre del equipo.
        ciudad (str): La ciudad de origen del equipo.
        director_tecnico (str): El nombre del director técnico del equipo.

    Retorno de datos:
        list: La lista de equipos actualizada si se registra el nuevo equipo, None si el equipo ya existe.
    """
    if equipo_existe(id_equipo):
        print(f"Error: Ya existe un equipo con el ID {id_equipo}.")
        return None
    
    equipo = {
        "id": id_equipo,
        "nombre": nombre,
        "ciudad": ciudad,
        "director_tecnico": director_tecnico,
        "estadisticas": {
            "puntos": 0,
            "jugados": 0,
            "ganados": 0,
            "empatados": 0,
            "perdidos": 0,
            "goles_favor": 0,
            "goles_contra": 0
        }
    }
    equipos.append(equipo)
    print(f"Equipo '{nombre}' registrado con éxito.")
    return equipos

# Función para buscar el equipo 
def buscar_equipo2(id_equipo):
    """Busca un equipo por su ID y devuelve su información si existe.
    Argumentos de entrada:
        id_equipo (str): El ID del equipo a registrar.

    Retorno de datos:
        Diccionario: Equipo almacenado en el JSON.
    """
    return next((e for e in equipos if e["id"] == id_equipo), None)                                                 

# Función para buscar el equipo por nombre
def buscar_equipo(criterio, valor):
    """
    Busca un equipo por su nombre y devuelve su información si existe.
    
    Argumentos de entrada:
        criterio (str): El criterio de búsqueda.
        valor (str): El valor a buscar para el criterio especificado.

    Retorno de datos:
        lista: Un diccionario con la información del equipo si existe, None en caso contrario.
    """
    return [equipo for equipo in equipos if str(equipo.get(criterio, "")).lower() == str(valor).lower()]    

# Función de actualizar información 
def actualizar_estadisticas_equipo(id_equipo, ganados, empatados, perdidos, goles_favor, goles_contra):
    """Actualiza las estadísticas de un equipo.
    
    Argumentos de entrada:
        id_equipo (int): El ID del equipo cuyas estadísticas se desean actualizar.
        ganados (int): Número de partidos ganados.
        empatados (int): Número de partidos empatados.
        perdidos (int): Número de partidos perdidos.
        goles_favor (int): Número de goles a favor del equipo.
        goles_contra (int): Número de goles en contra del equipo.

    Retorno de datos:
        None: Actualiza las estadísticas del equipo y no retorna ningún valor explícito.

    Lanza:
        ValueError: Si no se encuentra el equipo con el ID especificado.
    """
    equipo = buscar_equipo2(id_equipo)
    if equipo:
        equipo["estadisticas"]["jugados"] += ganados + empatados + perdidos
        equipo["estadisticas"]["ganados"] += ganados
        equipo["estadisticas"]["empatados"] += empatados
        equipo["estadisticas"]["perdidos"] += perdidos
        equipo["estadisticas"]["goles_favor"] += goles_favor
        equipo["estadisticas"]["goles_contra"] += goles_contra
        equipo["estadisticas"]["puntos"] += ganados * 3 + empatados
    else:
        raise ValueError("Equipo no encontrado.")

def verificar_numero_mayor_o_igual_a_cero(mensaje):
    """
    Solicita al usuario ingresar un número entero mayor o igual a cero.
    Permite dejar el campo en blanco para mantener el valor actual.

    Argumentos de entrada:
        mensaje (str): Mensaje para solicitar el número al usuario.

    Retorno de datos:
        int or None: El número ingresado si es mayor o igual a cero, o None si se deja en blanco.
    """
    while True:
        entrada = input(mensaje).strip()
        
        if entrada == "":
            return None  # Deja el campo en blanco para no cambiar el valor actual
            
        try:
            numero = int(entrada)
            if numero >= 0:
                return numero
            else:
                print("Error: El número debe ser mayor o igual a cero.")
        except ValueError:
            print("Error: Ingresa un número entero válido.")
