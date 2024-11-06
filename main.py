# Estas son las librerias creadas y utlizadas para el sistema de clases de futbol
from equipos import *
from jugadores import *
from partidos import *
from arbitros import *
from gestion import *
from reportes import *
import unicodedata
# Agregar comentarios de cada sección y en readme.md agregar la explicación de que contiene cada bloque

# Menú principal con lo solicitado de registrar, buscar, actualizar y visualizar reportes
def menu():
    """
    Muestra el menú principal de opciones para la gestión de equipos, jugadores, árbitros, 
    partidos y generación de reportes en el torneo. La función permite al usuario seleccionar 
    una de las opciones disponibles para acceder a submenús específicos o salir del programa.
    
    La función sigue en un bucle hasta que el usuario elige la opción de salir ('0').
    """

    while True:
        # Mostrar el encabezado del menú principal
        print("\n--- Menú Principal ---")
        print("1. Gestión de Equipos")   # Opción para gestionar los datos de los equipos
        print("2. Gestión de Jugadores") # Opción para gestionar los datos de los jugadores
        print("3. Gestión de Árbitros")  # Opción para gestionar los datos de los árbitros
        print("4. Gestión de Partidos")  # Opción para gestionar los datos de los partidos
        print("5. Generar Reportes")     # Opción para generar reportes del torneo
        print("0. Salir")                # Opción para salir del menú y finalizar el programa

        # Solicitar al usuario que seleccione una opción del menú
        opcion = input("Seleccione una opción: ")

        # Evaluar la opción ingresada por el usuario y llamar a la función correspondiente
        if opcion == '1':
            # Llama al menú de gestión de equipos.
            menu_equipos()
        elif opcion == '2':
            # Llama al menú de gestión de jugadores.
            menu_jugadores()
        elif opcion == '3':
            # Llama al menú de gestión de árbitros.
            menu_arbitros()
        elif opcion == '4':
            # Llama al menú de gestión de partidos.
            menu_partidos()
        elif opcion == '5':
            # Llama al menú de generación de reportes.
            menu_reportes()
        elif opcion == '0':
            # Si se selecciona '0', se muestra un mensaje de despedida y se termina el bucle
            print("¡Hasta luego!")
            break
        else:
            # Si la opción no es válida, muestra un mensaje de error y permite reintentar
            print("Opción no válida. Intente de nuevo.")

# Menú de equipos 
def menu_equipos():
    """
    Muestra un submenú para la gestión de equipos, permitiendo registrar nuevos equipos, 
    buscar información de un equipo existente, actualizar la información de un equipo 
    o volver al menú principal. La función continúa en un bucle hasta que el usuario 
    elige volver al menú principal.
    """

    while True:
        # Mostrar el encabezado del submenú de gestión de equipos
        print("\n--- Gestión de Equipos ---")
        print("1. Registrar nuevo equipo")            # Opción para registrar un nuevo equipo
        print("2. Buscar equipo")                     # Opción para buscar la información de un equipo por su ID
        print("3. Actualizar información de equipo")  # Opción para actualizar datos de un equipo existente
        print("4. Volver al menú principal")          # Opción para volver al menú principal

        # Solicitar al usuario que seleccione una opción del menú
        opcion = input("Seleccione una opción: ")

        # Opción 1: Registrar un nuevo equipo
        if opcion == '1':
            # Solicita al usuario los datos para el nuevo equipo
            id_equipo = "EQP"+str(verificar_numero("ID del equipo solo el número: "))
            nombre = verificar_string("Nombre del equipo: ").title()
            ciudad = verificar_ciudad_equipo()
            director_tecnico = verificar_string("Director técnico: ").title()
            
            # Llama a la función para registrar el equipo con los datos ingresados
            data = registrar_equipo(id_equipo, nombre, ciudad, director_tecnico)
            
            # Si se registra correctamente, guarda los datos en el archivo JSON correspondiente
            if data is not None:
                guardar_datos('data/equipos.json', data) 

        # Opción 2: Buscar un equipo
        elif opcion == '2':
            # Solicita el ID del equipo que se desea buscar
            criterio = verificar_string("Criterio del equipo que desea buscar: ").strip()
            valor = verificar_string("Valor del criterio que desea buscar: ").strip()
            
            # Llama a la función para buscar el equipo por su ID
            equipo = buscar_equipo(criterio, valor)
            
            # Si el equipo existe, muestra su información en pantalla
            for pos in range(len(equipo)):
                if equipo:
                    print(f"\nInformación del equipo {equipo[pos]['nombre']}:")
                    print(f"ID: {equipo[pos]['id']}, Ciudad: {equipo[pos]['ciudad']}, "
                        f"Director Técnico: {equipo[pos]['director_tecnico']}")
                else:
                    # Muestra un mensaje si no se encontró el equipo con el ID proporcionado
                    print(f"No se encontró ningún equipo con nombre {equipo}.")

        # Opción 3: Actualizar la información de un equipo
        elif opcion == '3':
            # Solicita el ID del equipo que se desea actualizar
            id_equipo = "EQP"+str(verificar_numero("Ingrese el ID (solo el número) del equipo a actualizar: "))
            print(f"\nID Ingresado es: {id_equipo}")
            # Llama a la función para buscar el equipo
            equipo = buscar_equipo2(id_equipo)
            
            if equipo:
                # Muestra la información actual del equipo antes de actualizarla
                print(f"\nInformación actual del equipo {equipo['nombre']}:")
                print(f"Ciudad: {equipo['ciudad']}, Director Técnico: {equipo['director_tecnico']}")

                # Solicita nuevos valores para las estadísticas del equipo, o mantiene los valores actuales si se dejan en blanco
                ganados = verificar_numero_mayor_o_igual_a_cero("Nueva cantidad de partidos ganados (deje vacío para no cambiar): ")
                equipo['estadisticas']['ganados'] = ganados if ganados is not None else equipo['estadisticas']['ganados']

                empatados = verificar_numero_mayor_o_igual_a_cero("Nueva cantidad de partidos empatados (deje vacío para no cambiar): ")
                equipo['estadisticas']['empatados'] = empatados if empatados is not None else equipo['estadisticas']['empatados']

                perdidos = verificar_numero_mayor_o_igual_a_cero("Nueva cantidad de partidos perdidos (deje vacío para no cambiar): ")
                equipo['estadisticas']['perdidos'] = perdidos if perdidos is not None else equipo['estadisticas']['perdidos']

                goles_favor = verificar_numero_mayor_o_igual_a_cero("Nueva cantidad de goles a favor (deje vacío para no cambiar): ")
                equipo['estadisticas']['goles_favor'] = goles_favor if goles_favor is not None else equipo['estadisticas']['goles_favor']

                goles_contra = verificar_numero_mayor_o_igual_a_cero("Nueva cantidad de goles en contra (deje vacío para no cambiar): ")
                equipo['estadisticas']['goles_contra'] = goles_contra if goles_contra is not None else equipo['estadisticas']['goles_contra']


                # Actualiza las estadísticas del equipo con los valores ingresados
                actualizar_estadisticas_equipo(id_equipo, ganados, empatados, perdidos, goles_favor, goles_contra)
                print(f"Equipo '{equipo['nombre']}' actualizado con éxito.")
                
                # Guarda los cambios en el archivo JSON
                guardar_datos('data/equipos.json', equipos) 
            else:
                # Muestra un mensaje si no se encontró el equipo con el ID proporcionado
                print(f"No se encontró ningún equipo con ID {id_equipo}.")

        # Opción 4: Volver al menú principal
        elif opcion == '4':
            # Finaliza el bucle para volver al menú principal
            print("Volviendo al menú principal...")
            break

        else:
            # Muestra un mensaje si se ingresó una opción que no es válida
            print("Opción no válida. Intente nuevamente.")

# Menú de jugadores
def menu_jugadores():
    """
    Muestra un submenú para la gestión de jugadores, permitiendo registrar nuevos jugadores, 
    buscar información de un jugador existente, actualizar la información de un jugador 
    o volver al menú principal. La función continúa en un bucle hasta que el usuario 
    elige volver al menú principal.
    """
    
    while True:
        # Mostrar el encabezado del submenú de gestión de jugadores
        print("\n--- Gestión de Jugadores ---")
        print("1. Registrar nuevo jugador")               # Opción para registrar un nuevo jugador
        print("2. Buscar jugador")                        # Opción para buscar la información de un jugador por su ID
        print("3. Actualizar información de un jugador")  # Opción para actualizar datos de un jugador existente
        print("4. Volver al menú principal")              # Opción para volver al menú principal

        # Solicitar al usuario que seleccione una opción del menú
        opcion = input("Seleccione una opción: ")

        # Opción 1: Registrar un nuevo jugador
        if opcion == "1":
            # Solicita al usuario los datos para el nuevo jugador
            id_jugador = "JUG"+str(verificar_numero("ID del jugador solo el número: "))
            nombre = verificar_string("Nombre del jugador: ")
            numero = verificar_numero("Número del jugador: ")
            posicion = verificar_posicion()
            equipo_id = str(verificar_numero("ID del equipo al que pertenece: "))            
            # Llama a la función para registrar el jugador con los datos ingresados
            data = registrar_jugador(id_jugador, nombre, numero, posicion, equipo_id)
            # Si se registra correctamente, guarda los datos en el archivo JSON correspondiente
            if data is not None:
                guardar_datos('data/jugadores.json', data)
    
        # Opción 2: Buscar un jugador
        elif opcion == "2":
            # Solicita el ID del jugador que se desea buscar
            criterio = verificar_string("Ingrese el criterio por el cual buscar el jugador a buscar (nombre, posición): ").strip()
            criterio = ''.join((c for c in unicodedata.normalize('NFD', criterio) if unicodedata.category(c) != 'Mn'))
            valor = verificar_string("Ingrese el valor del criterio, sea la posición o el nombre del jugador a buscar: ")
            
            # Llama a la función para buscar el jugador por su ID
            jugador = buscar_jugador(criterio, valor)
            
            # Si el jugador existe, muestra su información en pantalla
            for pos in range(len(jugador)):
                if jugador:
                    print(f"\nInformación actual del jugador {jugador[pos]['nombre']}:")
                    print(f"Goles: {jugador[pos]['estadisticas']['goles']}, Asistencias: {jugador[pos]['estadisticas']['asistencias']}, "
                        f"Amarillas: {jugador[pos]['estadisticas']['amarillas']}, Rojas: {jugador[pos]['estadisticas']['rojas']}, "
                        f"Minutos: {jugador[pos]['estadisticas']['minutos']}")
                else:
                    # Muestra un mensaje si no se encontró el jugador con el ID proporcionado
                    print(f"No se encontró ningún jugador.")

        # Opción 3: Actualizar la información de un jugador
        elif opcion == "3":
            # Solicita el ID del jugador que se desea actualizar
            id_jugador = "JUG"+str(verificar_numero("Ingrese el ID (solo el número) del jugador a actualizar: "))
            print(f"\nID Ingresado es: {id_jugador}")
            
            # Llama a la función para buscar el jugador
            jugador = buscar_jugador2(id_jugador)
            
            if jugador:
                # Muestra la información actual del jugador antes de actualizarla
                print(f"\nInformación actual del jugador {jugador['nombre']}:")
                print(f"Partidos: {jugador['estadisticas']['partidos']}, Goles: {jugador['estadisticas']['goles']}, "
                    f"Asistencias: {jugador['estadisticas']['asistencias']}, Amarillas: {jugador['estadisticas']['amarillas']}, "
                    f"Rojas: {jugador['estadisticas']['rojas']}, Minutos: {jugador['estadisticas']['minutos']}")

                # Solicita nuevos valores para las estadísticas del jugador o mantiene los valores actuales si se dejan en blanco

                # Actualización de goles
                while True:
                    goles_input = verificar_numero("Nueva cantidad de goles (deje vacío para no cambiar): ")
                    if goles_input == '':
                        goles = jugador['estadisticas']['goles']
                        break
                    else:
                        goles = int(goles_input)
                        if goles >= 0:
                            break
                        print("Error: La cantidad de goles no puede ser negativa. Intente de nuevo.")

                # Actualización de asistencias
                while True:
                    asistencias_input = verificar_numero("Nueva cantidad de asistencias (deje vacío para no cambiar): ")
                    if asistencias_input == '':
                        asistencias = jugador['estadisticas']['asistencias']
                        break
                    else:
                        asistencias = int(asistencias_input)
                        if asistencias >= 0:
                            break
                        print("Error: La cantidad de asistencias no puede ser negativa. Intente de nuevo.")

                # Actualización de amarillas
                while True:
                    amarillas_input = verificar_numero("Cantidad de amarillas (0 para no cambiar): ")
                    if amarillas_input == '0':
                        amarillas = jugador['estadisticas']['amarillas']
                        break
                    else:
                        amarillas = int(amarillas_input)
                        if amarillas >= 0:
                            break
                        print("Error: La cantidad de amarillas no puede ser negativa. Intente de nuevo.")

                # Actualización de rojas
                while True:
                    rojas_input = verificar_numero("Cantidad de rojas (0 para no cambiar): ")
                    if rojas_input == '0':
                        rojas = jugador['estadisticas']['rojas']
                        break
                    else:
                        rojas = int(rojas_input)
                        if rojas >= 0:
                            break
                        print("Error: La cantidad de rojas no puede ser negativa. Intente de nuevo.")

                # Actualización de minutos
                while True:
                    minutos_input = verificar_numero("Cantidad de minutos (0 para no cambiar): ")
                    if minutos_input == '0':
                        minutos = jugador['estadisticas']['minutos']
                        break
                    else:
                        minutos = int(minutos_input)
                        if minutos >= 0:
                            break
                        print("Error: La cantidad de minutos no puede ser negativa. Intente de nuevo.")


                # Actualiza las estadísticas del jugador con los valores ingresados
                actualizar_estadisticas_jugador(jugador, goles, asistencias, amarillas, rojas, minutos)
                print(f"Jugador '{jugador['nombre']}' actualizado con éxito.")
                
                # Guarda los cambios en el archivo JSON
                guardar_datos('data/jugadores.json', jugadores)
            else:
                # Muestra un mensaje si no se encontró el jugador con el ID proporcionado
                print(f"No se encontró ningún jugador con ID {id_jugador}.")

        # Opción 4: Volver al menú principal
        elif opcion == "4":
            # Finaliza el bucle para volver al menú principal
            print("Saliendo del menú de gestión de jugadores.")
            break

        else:
            # Muestra un mensaje si se ingresó una opción que no es válida
            print("Opción no válida, por favor intente de nuevo.")

# Menú de arbitros
def menu_arbitros():
    """
    Muestra un submenú para la gestión de árbitros, permitiendo al usuario registrar nuevos árbitros, 
    buscar árbitros existentes, y actualizar su información. La función sigue en bucle hasta que el 
    usuario elige volver al menú principal.
    """

    while True:
        # Mostrar el encabezado del submenú de gestión de árbitros
        print("\n--- Gestión de Árbitros ---")
        print("1. Registrar nuevo árbitro")               # Opción para registrar un árbitro nuevo
        print("2. Buscar árbitro")                        # Opción para buscar información sobre un árbitro registrado
        print("3. Asignar árbitro a un partido")          # Opción para asignar un arbitro a un partido
        print("4. Actualizar información de un árbitro")  # Opción para actualizar datos de un árbitro
        print("5. Volver al menú principal")              # Opción para salir del submenú y volver al menú principal

        # Solicitar al usuario que seleccione una opción del menú de gestión de árbitros
        opcion = input("Seleccione una opción: ")
        
        # Opción 1: Registrar nuevo árbitro
        if opcion == "1":
            # Solicitar y verificar la entrada de datos para registrar un nuevo árbitro
            id_arbitro = "ARB"+str(verificar_numero("ID del árbitro solo el número: "))
            nombre = verificar_string("Nombre del árbitro: ")
            experiencia = verificar_numero("Años de experiencia del árbitro: ")
            categoria = verificar_categoria_arbitro()

            # Registrar el árbitro y guardar los datos si se registra con éxito
            data = registrar_arbitro(id_arbitro, nombre, experiencia, categoria)
            if data is not None:
                guardar_datos('data/arbitros.json', data)

        # Opción 2: Buscar un árbitro registrado
        elif opcion == "2":
            # Solicitar el ID del árbitro y buscarlo en los registros
            nombre_arbitro = verificar_string("Ingrese el nombre del árbitro a buscar: ").title().strip()
            arbitro = buscar_arbitro(nombre_arbitro)

            if arbitro:
                # Mostrar la información del árbitro si existe
                print(f"\nInformación del árbitro {arbitro['nombre']}:")
                print(f"Experiencia: {arbitro['experiencia']}, "
                      f"Categoría: {arbitro['categoria']}, "
                      f"Partidos dirigidos: {arbitro['partidos_dirigidos']}")
            else:
                print(f"No se encontró ningún árbitro con nombre {nombre_arbitro}.")

        # Opción 3: Asignar un árbitro a un partido
        elif opcion == "3":
            # Solicitar el ID del árbitro y el ID del partido
            id_arbitro = "ARB"+verificar_string("Ingrese solo el número de ID del árbitro a asignar: ")
            id_partido = "PAR"+verificar_string("Ingrese solo el número ID del partido a asignar: ")
            fecha = verificar_string("Fecha del partido (YYYY-MM-DD): ")
            # Asignar el árbitro al partido y guardar los datos si se asigna
            Asignar_arbitro(id_partido, id_arbitro, fecha)

        # Opción 4: Actualizar información de un árbitro
        elif opcion == "4":
            # Solicitar el ID del árbitro y verificar que exista
            id_arbitro = "ARB"+str(verificar_numero("Ingrese el ID (solo el número) del árbitro a actualizar: "))
            arbitro = buscar_arbitro(id_arbitro)

            if arbitro:
                # Mostrar la información actual del árbitro antes de actualizar
                print(f"\nInformación actual del árbitro {arbitro['nombre']}:")
                print(f"Experiencia: {arbitro['experiencia']}, Categoría: {arbitro['categoria']}, "
                      f"Partidos dirigidos: {arbitro['partidos_dirigidos']}")

                # Solicitar nuevos datos; si el usuario deja en blanco, se conserva el valor actual
                experiencia = verificar_numero("Nueva experiencia en años (0 para no cambiar): ") or arbitro['experiencia']
                experiencia = int(experiencia) if experiencia != '' else arbitro['experiencia']
                categoria = input("Nueva categoría (deje vacío para no cambiar): ").title() or arbitro['categoria']

                # Actualizar los datos del árbitro y guardar los cambios
                actualizar_partidos_arbitro(arbitro, experiencia, categoria)
                guardar_datos('data/arbitros.json', arbitros)

            else:
                print(f"No se encontró ningún árbitro con ID {id_arbitro}.")

        # Opción 5: Volver al menú principal
        elif opcion == "5":
            # Finaliza el bucle para salir del menú de gestión de árbitros
            print("Saliendo del menú de gestión de árbitros.")
            break

        else:
            # Mensaje de error si se ingresa una opción no válida
            print("Opción no válida, por favor intente de nuevo.")

# Menú de partidos
def menu_partidos():
    """
    Muestra un submenú para la gestión de partidos, permitiendo al usuario registrar nuevos partidos, 
    buscar partidos existentes, actualizar resultados y registrar eventos. La función sigue en bucle 
    hasta que el usuario elige volver al menú principal.
    """
    
    while True:
        # Mostrar el encabezado del submenú de gestión de partidos
        print("\n--- Gestión de Partidos ---")
        print("1. Registrar nuevo partido")         # Opción para registrar un partido nuevo
        print("2. Buscar partido")                  # Opción para buscar información sobre un partido registrado
        print("3. Actualizar resultados")           # Opción para actualizar los resultados de un partido
        print("4. Registrar evento en un partido")  # Opción para registrar eventos específicos en un partido
        print("5. Volver al menú principal")        # Opción para salir del submenú y volver al menú principal

        # Solicitar al usuario que seleccione una opción del menú de gestión de partidos
        opcion = input("Seleccione una opción: ")

        # Opción 1: Registrar nuevo partido
        if opcion == "1":
            # Solicitar y verificar la entrada de datos para registrar un nuevo partido
            id_partido = "PAR"+str(verificar_numero("Ingrese solo el número ID del partido: "))
            fecha = verificar_string("Fecha del partido (YYYY-MM-DD): ")
            id_arbitro = "ARB"+str(verificar_numero("Ingrese solo el número de ID del árbitro: "))
            equipo_local = verificar_string("Equipo local: ")
            equipo_visitante = verificar_string("Equipo visitante: ")

            # Registrar el partido y guardar los datos si se registra con éxito
            data = registrar_partido(id_partido, fecha, id_arbitro, equipo_local, equipo_visitante)
            # gregar los alinemientos de equipo local y visitante
            agregar_alineacion(id_partido)
            
            if data is not None:
                guardar_datos('data/partidos.json', data)

        # Opción 2: Buscar un partido registrado
        elif opcion == "2":
            # Solicitar el ID del partido y buscarlo en los registros
            id_partido = verificar_numero("Ingrese el ID del partido a buscar: ")
            buscar_partido(id_partido)

        # Opción 3: Actualizar datos del partido
        elif opcion == "3":
            # Solicitar el ID del partido y los resultados para actualizarlos en el registro
            id_partido = "PAR"+str(verificar_numero("Ingrese solo el número del ID del partido a actualizar: "))
            goles_local = verificar_numero("Goles del equipo local: ")
            goles_visitante = verificar_numero("Goles del equipo visitante: ")

            # Actualizar los resultados y guardar los datos
            actualizar_resultados(id_partido, goles_local, goles_visitante)
            guardar_datos('data/partidos.json', partidos)

        # Opción 4: Registrar evento en un partido
        elif opcion == "4":
            # Solicitar detalles del evento, como minuto, tipo de evento, jugador involucrado y equipo
            id_partido = "PAR"+str(verificar_numero("Ingrese solo el número del ID del partido: "))
            minuto = verificar_numero("Minuto del evento: ")
            tipo_evento = verificar_string("Tipo de evento (gol, tarjeta, sustitución, etc.): ").title()
            jugador = verificar_string("Jugador involucrado: ").title()
            equipo = verificar_string("Equipo del jugador: ").title()

            # Registrar el evento en el partido correspondiente y guardar los datos
            registrar_evento(id_partido, minuto, tipo_evento, jugador, equipo)
            guardar_datos('data/partidos.json', partidos)

        # Opción 5: Volver al menú principal
        elif opcion == "5":
            # Finaliza el bucle para salir del menú de gestión de partidos
            print("Saliendo del menú de gestión de partidos.")
            break

        else:
            # Mensaje de error si se ingresa una opción no válida
            print("Opción no válida, por favor intente de nuevo.")

# Menú de reportes
def menu_reportes():
    """
    Muestra un submenú para la generación de reportes, permitiendo al usuario seleccionar 
    entre generar una tabla de posiciones, una lista de goleadores, un reporte de árbitros 
    o volver al menú principal. La función permanece en un bucle hasta que el usuario elige 
    salir al menú principal.
    """
    
    while True:
        # Mostrar el encabezado del submenú de generación de reportes
        print("\n--- Generación de Reportes ---")
        print("1. Tabla de posiciones")       # Opción para generar y mostrar la tabla de posiciones
        print("2. Lista de goleadores")       # Opción para generar y mostrar la lista de goleadores
        print("3. Reporte de árbitros")       # Opción para generar y mostrar el reporte de árbitros
        print("4. Reporte general de equipos")# Opción para generar el reporte general de los equipos
        print("5. Volver al menú principal")  # Opción para salir al menú de reportes y volver al menú principal

        # Solicitar al usuario que seleccione una opción del menú de reportes
        opcion = input("Seleccione una opción: ")

        # Opción 1: Generar la tabla de posiciones
        if opcion == '1':
            # Llama a la función para generar y mostrar la tabla de posiciones de los equipos
            generar_tabla_posiciones()

        # Opción 2: Generar la lista de goleadores
        elif opcion == '2':
            # Llama a la función para generar y mostrar la lista de goleadores
            while True:
                try:
                    cantidad = int(input("Ingresa la cantidad de goleadores a visualizar, ingresa un número entero mayor o igual a 0: "))
                    if cantidad < 0:
                        print("Error: El número no puede ser negativo.")
                    else:
                        generar_lista_goleadores(cantidad)
                        break
                except ValueError:
                    print("Error: Por favor, ingresa un número entero válido.")

        # Opción 3: Generar el reporte de árbitros
        elif opcion == '3':
            # Llama a la función para generar y mostrar el reporte de los árbitros
            generar_reporte_arbitros()
        
        # Opción 4: Generar el reporte de estagísticas de equipos
        elif opcion == '4':
            # Llama a la función para generar y mostrar el reporte de los árbitros
            generar_estadisticas_equipo()

        # Opción 5: Volver al menú principal
        elif opcion == "5":
            # Finaliza el bucle para salir del menú de reportes y volver al menú principal
            print("Saliendo del menú de generación de reportes.")
            break

        else:
            # Muestra un mensaje si se ingresa una opción no válida
            print("Opción no válida.")

# Iniciación del menú principal
if __name__ == "__main__":
    menu()
