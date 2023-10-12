import time
from habbo_launcher import HabboLauncher

def rastrear_y_clickear_furni(nombre_furni, cantidad_clics, nombre_sala):
    launcher = HabboLauncher("1.0.30")  # Inicializar el Habbo Launcher

    # Iniciar sesión en Habbo
    launcher.login("nombre_de_usuario", "contraseña")

    while True:
        # Esperar a que aparezca el furni en la sala
        while not launcher.furni_aparecido(nombre_furni, nombre_sala):
            time.sleep(1)  # Esperar a que aparezca el furni

        # Rastrear el furni y darle clic 10 veces
        for _ in range(cantidad_clics):
            while not launcher.esta_cerca_furni(nombre_furni):
                time.sleep(1)  # Esperar a acercarse al furni

            launcher.clickear_furni(nombre_furni)

    launcher.cerrar_sesion()  # Cerrar sesión en Habbo

# Ejemplo de uso
rastrear_y_clickear_furni("nombre_del_furni", 10, "nombre_de_sala")
