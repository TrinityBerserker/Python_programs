import os

def ordenar_archivos_por_nombre(ruta_carpeta):
    # Verificar si la ruta es válida y es un directorio
    if not os.path.isdir(ruta_carpeta):
        print(f"La ruta especificada '{ruta_carpeta}' no es un directorio válido.")
        return
    
    # Obtener la lista de archivos en la carpeta
    archivos = os.listdir(ruta_carpeta)
    
    # Ordenar los archivos por nombre (orden alfabético)
    archivos.sort()
    
    # Mostrar los archivos ordenados
    print(f"Archivos en '{ruta_carpeta}', ordenados alfabéticamente:")
    for archivo in archivos:
        print(archivo)

# Solicitar la ruta de la carpeta al usuario
ruta = input("Ingrese la ruta de la carpeta que desea ordenar: ")

# Llamar a la función para ordenar y mostrar los archivos
ordenar_archivos_por_nombre(ruta)
