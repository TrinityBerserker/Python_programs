# Definir el tablero de ajedrez
tablero = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))

# Función para mover una pieza en el tablero
def mover_pieza(origen, destino):
    x_origen, y_origen = origen
    x_destino, y_destino = destino

    pieza = tablero[x_origen][y_origen]
    tablero[x_origen][y_origen] = ' '
    tablero[x_destino][y_destino] = pieza

# Función para validar un movimiento
def validar_movimiento(origen, destino, jugador):
    x_origen, y_origen = origen
    x_destino, y_destino = destino

    # Verificar si la casilla de origen contiene una pieza del jugador actual
    if tablero[x_origen][y_origen].islower() != jugador.islower():
        return False
    
    # Lógica para validar movimientos específicos de cada tipo de pieza
    # ...

    return True

# Función para obtener las posibles casillas de destino para una pieza
def obtener_posibles_destinos(origen):
    x_origen, y_origen = origen

    # Lógica para obtener los posibles destinos según el tipo de pieza
    # ...

    return posibles_destinos

# Función para jugar una partida de ajedrez
def jugar_partida():
    jugador_actual = 'blanco'  # Jugador actual ('blanco' o 'negro')

    while True:
        # Imprimir el tablero actual
        imprimir_tablero(tablero)

        # Obtener la entrada del jugador para el movimiento
        entrada = input(f"Jugador {jugador_actual}, ingrese su movimiento (ejemplo: a2 a4): ")
        origen, destino = entrada.split()

        # Convertir las coordenadas de la entrada en índices de la matriz
        x_origen = 8 - int(origen[1])
        y_origen = ord(origen[0]) - ord('a')
        x_destino = 8 - int(destino[1])
        y_destino = ord(destino[0]) - ord('a')

        # Validar el movimiento
        if validar_movimiento((x_origen, y_origen), (x_destino, y_destino), jugador_actual):
            mover_pieza((x_origen, y_origen), (x_destino, y_destino))
        else:
            print("Movimiento inválido. Intenta de nuevo.")

        # Cambiar al siguiente jugador
        jugador_actual = 'negro' if jugador_actual == 'blanco' else 'blanco'

# Iniciar la partida
jugar_partida()
