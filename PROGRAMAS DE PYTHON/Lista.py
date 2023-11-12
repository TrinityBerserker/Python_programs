# Crear una lista vacía para almacenar la asistencia
asistencia = []

while True:
    # Solicitar al usuario que ingrese el nombre del estudiante o 'q' para salir
    nombre = input("Ingresa el nombre del estudiante (o 'q' para salir): ")

    if nombre.lower() == 'q':
        break  # Salir del bucle si se ingresa 'q'
    
    # Agregar el nombre del estudiante a la lista de asistencia
    asistencia.append(nombre)

# Mostrar la lista de asistencia
print("Lista de Asistencia:")
for estudiante in asistencia:
    print(estudiante)

# Guardar la lista de asistencia en un archivo de texto
with open("asistencia.txt", "w") as archivo:
    for estudiante in asistencia:
        archivo.write(estudiante + "\n")

print("La lista de asistencia se ha guardado en 'asistencia.txt'.")
