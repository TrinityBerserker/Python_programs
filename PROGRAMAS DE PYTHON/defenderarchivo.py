import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Carpeta a monitorear
folder_to_watch = "C:/Users/Username/Desktop/FirewallFolder"

# Función para verificar si un archivo es sospechoso
def is_suspicious(file_path):
    # Implementación básica de detección: solo verifica la extensión
    suspicious_extensions = ['.exe', '.bat', '.vbs', '.js']  # Ejemplo de extensiones sospechosas
    
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() in suspicious_extensions:
        return True
    return False

# Manejador de eventos para el monitor de la carpeta
class FolderMonitor(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            if is_suspicious(file_path):
                print(f"Archivo sospechoso detectado: {file_path}")
                # Aquí podrías implementar acciones como mover el archivo a cuarentena
                # shutil.move(file_path, "ruta a carpeta de cuarentena")
            else:
                print(f"Archivo seguro detectado: {file_path}")

# Función principal para iniciar el monitoreo
def start_firewall():
    event_handler = FolderMonitor()
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=True)
    observer.start()
    print(f"Monitoreando la carpeta: {folder_to_watch}")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_firewall()
