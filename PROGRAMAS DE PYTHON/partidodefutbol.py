import random

# Nombres de los equipos
equipo_local = "Equipo Local"
equipo_visitante = "Equipo Visitante"

# Inicialización de marcadores
marcador_local = 0
marcador_visitante = 0

# Comentario del inicio del partido
print(f"¡Bienvenidos al partido entre {equipo_local} y {equipo_visitante}!")
print("El partido está a punto de comenzar...\n")

# Simulación de tiempo en minutos
tiempo = 0

# Duración del partido en minutos
duracion_partido = 90

while tiempo < duracion_partido:
    # Generar un evento aleatorio
    evento = random.choice(["Pase", "Tiro al arco", "Falta", "Gol", "Córner", "Saque de banda"])

    # Comentar el evento
    if evento == "Pase":
        print(f"{tiempo}' - {equipo_local} hace un pase hacia el mediocampo.")
    elif evento == "Tiro al arco":
        if random.random() < 0.3:  # 30% de probabilidad de marcar un gol
            print(f"{tiempo}' - ¡GOOOL! {equipo_local} marca un gol.")
            marcador_local += 1
        else:
            print(f"{tiempo}' - {equipo_local} tira al arco pero el portero atrapa el balón.")
    elif evento == "Falta":
        print(f"{tiempo}' - Falta cometida por {equipo_visitante}.")
    elif evento == "Gol":
        print(f"{tiempo}' - ¡GOOOL! {equipo_visitante} marca un gol.")
        marcador_visitante += 1
    elif evento == "Córner":
        print(f"{tiempo}' - {equipo_local} gana un córner.")
    elif evento == "Saque de banda":
        print(f"{tiempo}' - {equipo_visitante} realiza un saque de banda.")

    tiempo += 1

# Comentario final del partido
print("\n¡Final del partido!")
print(f"Resultado: {equipo_local} {marcador_local} - {equipo_visitante} {marcador_visitante}")
