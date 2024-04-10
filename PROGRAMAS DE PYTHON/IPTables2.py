import subprocess

def permitir_ssh():
    comando = "iptables -A INPUT -p tcp --dport 22 -j ACCEPT"
    subprocess.run(comando, shell=True)

permitir_ssh()
