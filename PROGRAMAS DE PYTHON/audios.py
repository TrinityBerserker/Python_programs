import speech_recognition as sr

def reconocer_voz():
    # Crear un objeto de reconocimiento de voz
    r = sr.Recognizer()

    # Escuchar el audio del micrófono
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)

    # Intentar reconocer el texto
    try:
        texto = r.recognize_google(audio, language="es")
        print("Has dicho: " + texto)
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio")
    except sr.RequestError as e:
        print("Error al realizar la solicitud: {0}".format(e))

# Llamar a la función para iniciar el reconocimiento de voz
reconocer_voz()
