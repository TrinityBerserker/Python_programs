import subprocess

def establecer_regla_personalizada(ip_origen, ip_destino, puerto, accion):
    comando = f"iptables -A INPUT -s {ip_origen} -d {ip_destino} -p tcp --dport {puerto} -j {accion}"
    subprocess.run(comando, shell=True)

establecer_regla_personalizada("192.168.1.100", "192.168.1.200", 22, "ACCEPT")

