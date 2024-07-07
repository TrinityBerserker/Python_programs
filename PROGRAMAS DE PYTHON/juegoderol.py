def print_welcome_message():
    print("""
    ====================================
    Bienvenido al Juego de Aventura Textual
    ====================================
    """)
    print("""
              _.--.
          _.-'_:-'||
      _.-'_.-::::'||
 _.-:'_.-::::::'  ||
.'`-.-:::::::'     ||
/.'`;|:::::::'      ||_
||   ||::::::'     _.;._'-._
||   ||:::::'  _.-!oo @.!-._'-.
\\'.  ||:::::.-!()oo @!()@.-'_.|
'.'-;|:.-'.&$@.& ()$%-'o.'\\U||
  `>'-.!@%()@'@_%-'_.-o _.|'||
   ||-._'-.@.-'_.-' _.-o  |'||
   ||=[ '-._.-\\U/.-'    o |'||
   || '-.]=|| |'|      o  |'||
   ||      || |'|        _| ';
   ||      || |'|    _.-'_.-'
   |'-._   || |'|_.-'_.-'
    '-._'-.|| |' `_.-'
        '-.||_/.-'
    """)

def make_choice(prompt, options):
    choice = None
    while choice not in options:
        print(prompt)
        for key, value in options.items():
            print(f"{key}: {value}")
        choice = input("Elige una opción: ").strip().lower()
    return choice

def cave_adventure():
    print("Te despiertas en una cueva oscura. Hay dos túneles frente a ti.")
    choice = make_choice("¿Cuál túnel tomas?", {'a': 'Túnel izquierdo', 'b': 'Túnel derecho'})

    if choice == 'a':
        print("Caminas por el túnel izquierdo y encuentras un cofre.")
        choice = make_choice("¿Abres el cofre?", {'a': 'Sí', 'b': 'No'})

        if choice == 'a':
            print("¡Encuentras un tesoro! Sigues adelante y ves una luz al final del túnel.")
            forest_adventure()
        else:
            print("Decides no abrir el cofre y continúas caminando.")
            print("Te pierdes en la oscuridad y encuentras una bifurcación.")
            choice = make_choice("¿Qué dirección tomas?", {'a': 'Izquierda', 'b': 'Derecha'})

            if choice == 'a':
                print("Encuentras una salida de la cueva, pero estás en un bosque oscuro.")
                forest_adventure()
            else:
                print("Te encuentras con un dragón. Has perdido el juego.")
    else:
        print("Caminas por el túnel derecho y te encuentras con un dragón.")
        choice = make_choice("¿Luchas contra el dragón?", {'a': 'Sí', 'b': 'No'})

        if choice == 'a':
            print("Luchas valientemente, pero el dragón es demasiado fuerte. Has perdido el juego.")
        else:
            print("Huyes rápidamente y encuentras una salida de la cueva. Has sobrevivido.")
            forest_adventure()

def forest_adventure():
    print("Te encuentras en un bosque denso. Hay un sendero que se divide en dos.")
    choice = make_choice("¿Qué camino tomas?", {'a': 'Sendero izquierdo', 'b': 'Sendero derecho'})

    if choice == 'a':
        print("Sigues el sendero izquierdo y encuentras una cabaña.")
        choice = make_choice("¿Entras a la cabaña?", {'a': 'Sí', 'b': 'No'})

        if choice == 'a':
            print("Entras a la cabaña y encuentras provisiones. Recuperas fuerzas y decides explorar más.")
            mountain_adventure()
        else:
            print("Decides no entrar a la cabaña y sigues caminando.")
            print("Te pierdes en el bosque y nunca encuentras la salida. Has perdido el juego.")
    else:
        print("Sigues el sendero derecho y encuentras un río.")
        river_adventure()

def river_adventure():
    print("Te encuentras en un río caudaloso. Hay un puente y un bote.")
    choice = make_choice("¿Qué decides hacer?", {'a': 'Cruzar el puente', 'b': 'Usar el bote'})

    if choice == 'a':
        print("Cruzas el puente y llegas a una aldea. Los aldeanos te ayudan y finalmente encuentras el camino a casa. ¡Has ganado el juego!")
    else:
        print("Usas el bote, pero la corriente es muy fuerte y el bote se vuelca. Has perdido el juego.")

def mountain_adventure():
    print("Te encuentras al pie de una montaña. Hay un sendero empinado y una cueva.")
    choice = make_choice("¿Qué decides hacer?", {'a': 'Subir la montaña', 'b': 'Entrar en la cueva'})

    if choice == 'a':
        print("Subes la montaña y encuentras un monasterio. Los monjes te ofrecen refugio y sabiduría.")
        choice = make_choice("¿Aceptas quedarte con los monjes?", {'a': 'Sí', 'b': 'No'})

        if choice == 'a':
            print("Aprendes mucho de los monjes y encuentras paz interior. Has encontrado un nuevo hogar. ¡Has ganado el juego!")
        else:
            print("Decides seguir tu camino y desciendes por el otro lado de la montaña, encontrando una nueva aventura.")
            print("Encuentras un valle lleno de vida y decides establecerte allí. ¡Has ganado el juego!")
    else:
        print("Entras en la cueva y encuentras un lago subterráneo.")
        choice = make_choice("¿Nadas a través del lago?", {'a': 'Sí', 'b': 'No'})

        if choice == 'a':
            print("Nadas a través del lago y encuentras una salida secreta. Te lleva a un hermoso jardín.")
            choice = make_choice("¿Exploras el jardín?", {'a': 'Sí', 'b': 'No'})

            if choice == 'a':
                print("Exploras el jardín y encuentras una comunidad secreta de sabios. Aprendes de ellos y vives en armonía. ¡Has ganado el juego!")
            else:
                print("Decides no explorar el jardín y sigues adelante.")
                print("Encuentras un desierto y te pierdes en la arena. Has perdido el juego.")
        else:
            print("Decides no nadar y vuelves al pie de la montaña.")
            mountain_adventure()

def start_adventure():
    print_welcome_message()
    cave_adventure()

if __name__ == "__main__":
    start_adventure()
