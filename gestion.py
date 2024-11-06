# Importar librerias utilizadas para el proceso
import os
import json

# Función par cargar los datos de un archivo .json
def cargar_datos(ruta):
    """
    Carga datos desde un archivo JSON. Si no existe, crea un archivo vacío.

    Argumento de entrada:
        ruta (str): Ruta del archivo JSON a cargar.

    Retorno de datos:
        list: Devuelve los datos cargados desde el archivo JSON. Si el archivo no existe, devuelve una lista vacía.
    """
    if os.path.exists(ruta):
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    else:
        print(f"No se encontró {ruta}, creando un archivo vacío.")
        # Crear un archivo vacío JSON
        with open(ruta, 'w') as archivo:
            json.dump([], archivo)  # Escribir una lista vacía en el archivo
        return []

# Función para guardar los datos en un archivo de formato .json
def guardar_datos(ruta, datos):
    """
    Guarda los datos en un archivo JSON.

    Argumentos de entrada:
        ruta (str): Ruta del archivo JSON donde se guardarán los datos.
        datos (list): Datos a guardar en el archivo JSON.

    Retorno de datos:
        None: La función no retorna ningún valor, solo guarda los datos en el archivo.
    """
    with open(ruta, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

# Función para verificar que se agrega un número 
def verificar_numero(messege):
    """
    Solicita al usuario ingresar un número entero y verifica su validez.

    Argumento de entrada:
        messege (str): Mensaje que se mostrará al usuario para solicitar el número.

    Retorno de datos:
        int: Devuelve el número entero ingresado por el usuario si es válido.
    """
    while True:
        entrada = input(messege)
        try:
            return int(entrada)  # Intentamos convertir a entero
        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")

# Función para verificar si ingresa un string
def verificar_string(messege):
    """
    Solicita al usuario ingresar una cadena de texto y verifica que no esté vacía.

    Argumento de entrada:
        messege (str): Mensaje que se mostrará al usuario para solicitar la cadena.

    Retorno de datos:
        str: Devuelve la cadena de texto ingresada por el usuario si es válida.
    """
    while True:
        entrada = input(messege).strip()  # Quitamos espacios al inicio y al final
        if entrada:  # Verifica si no está vacío
            return entrada
        else:
            print("Error: Por favor, ingresa una cadena de texto válida.")

# Función para verificar que el número sea mayor a cero
def verificar_numero_no_negativo():
    """
    Solicita al usuario ingresar un número entero mayor o igual a 0 y verifica su validez.

    Retorno de datos:
        int: Devuelve el número entero ingresado por el usuario si es válido y no negativo.
    """
    while True:
        try:
            numero = int(input("Ingresa un número entero mayor o igual a 0: "))
            if numero >= 0:
                return numero  # Retorna el número si es válido
            else:
                print("Error: El número no puede ser negativo.")
        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")

# Función verificadora de la ciudad del equipo
def verificar_ciudad_equipo():
    """
    Solicita al usuario ingresar el nombre de una ciudad y verifica si es válida
    (es decir, si tiene un equipo de fútbol profesional en Colombia).

    Retorno de datos:
        str: Devuelve el nombre de la ciudad ingresada por el usuario si es válida.
    """
    ciudades_validas = [
        "Bogotá", "Medellín", "Cali", "Barranquilla", "Manizales", 
        "Bucaramanga", "Pereira", "Ibagué", "Cúcuta", "Santa Marta", 
        "Neiva", "Tunja", "Villavicencio", "Montería", "Pasto", 
        "Rionegro", "Envigado"
    ]  # Lista de ciudades con equipos de fútbol profesional

    while True:
        print('\n------Nombre de las ciudades disponibles------')
        print(ciudades_validas)
        ciudad = input("Ingresa una ciudad con equipo de fútbol: ").title().strip().capitalize()
        if ciudad in ciudades_validas:
            return ciudad  # Retorna la ciudad si es válida
        else:
            print("Error: Ciudad no válida. Ingresa una ciudad que tenga un equipo de fútbol profesional en Colombia.")
