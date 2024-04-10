import requests
from googlesearch import search
from bs4 import BeautifulSoup

# Función para realizar la búsqueda en Google y obtener la respuesta con explicación y fuente
def buscar_respuesta(pregunta):
    # Realizar la búsqueda en Google
    resultados = search(pregunta, num_results=1, lang="es")

    # Obtener el primer resultado de la búsqueda
    respuesta = next(resultados, None)

    # Realizar solicitud HTTP para obtener el contenido de la página web
    response = requests.get(respuesta)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Verificar si se encontró una explicación
    explicacion = soup.find('div', {'class': 'ZINbbc xpd O9g5cc uUPGi'})
    if explicacion:
        # Obtener el texto de la explicación
        explicacion = explicacion.text
    else:
        # Mensaje de error en caso de no encontrar una explicación
        explicacion = "Lo siento, no se encontró una explicación para esta pregunta."

    # Obtener la fuente de la respuesta
    fuente = soup.find('cite').text

    # Devolver la respuesta, explicación y fuente
    return respuesta, explicacion, fuente

# Preguntar al asistente
pregunta = input("Hazme una pregunta: ")

# Realizar la búsqueda y obtener la respuesta, explicación y fuente
respuesta, explicacion, fuente = buscar_respuesta(pregunta)

# Mostrar la respuesta, explicación y fuente
print("Respuesta:", respuesta)
print("Explicación:", explicacion)
print("Fuente:", fuente)
