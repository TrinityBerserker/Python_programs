import subprocess

# Función para agregar una regla al firewall IPTables
def agregar_regla(accion, protocolo, puerto):
    comando = f"iptables -A INPUT -p {protocolo} --dport {puerto} -j {accion}"
    subprocess.run(comando, shell=True)

# Función para eliminar una regla del firewall IPTables
def eliminar_regla(accion, protocolo, puerto):
    comando = f"iptables -D INPUT -p {protocolo} --dport {puerto} -j {accion}"
    subprocess.run(comando, shell=True)

# Agregar una regla para permitir conexiones TCP en el puerto 80 (HTTP)
agregar_regla("ACCEPT", "tcp", 80)

# Eliminar la regla anterior
eliminar_regla("ACCEPT", "tcp", 80)
