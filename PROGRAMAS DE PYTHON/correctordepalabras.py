import enchant

def corregir_ortografia(archivo):
    # Crear un diccionario de verificación ortográfica en inglés
    d = enchant.Dict("en_US")
    
    # Leer el contenido del archivo
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Dividir el contenido en palabras
    palabras = contenido.split()
    
    # Lista para almacenar las correcciones realizadas
    correcciones = []
    
    # Verificar ortografía y corregir palabras incorrectas
    for palabra in palabras:
        if not d.check(palabra):  # Si la palabra no está en el diccionario
            sugerencias = d.suggest(palabra)  # Obtener sugerencias de corrección
            if sugerencias:
                correccion = sugerencias[0]  # Tomar la primera sugerencia como corrección
                correcciones.append((palabra, correccion))  # Guardar la palabra original y la corrección
                contenido = contenido.replace(palabra, correccion)  # Reemplazar en el contenido
    
    # Mostrar el contenido corregido por consola
    print("Texto corregido:")
    print(contenido)
    
    # Mostrar las correcciones realizadas
    print("\nCorrecciones realizadas:")
    for original, corregida in correcciones:
        print(f"{original} -> {corregida}")

# Solicitar al usuario el archivo que desea revisar
archivo = input("Ingrese el nombre del archivo que desea revisar (incluyendo la ruta si no está en el mismo directorio): ")

# Llamar a la función para corregir ortografía y mostrar correcciones
corregir_ortografia(archivo)
