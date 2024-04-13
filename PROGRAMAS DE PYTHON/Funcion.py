def saludar_persona():
    nombre = input("Por favor, ingresa tu nombre: ")
    mensaje = f"Hola, {nombre}! ¡Bienvenido!"
    return mensaje

saludo = saludar_persona()
print(saludo)
