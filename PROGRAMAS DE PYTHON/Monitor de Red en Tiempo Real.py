from scapy.all import sniff, IP, TCP, UDP

# Función de callback para manejar los paquetes capturados
def packet_callback(packet):
    # Si el paquete tiene una capa IP
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        # Si el paquete tiene una capa TCP
        if TCP in packet:
            tcp_sport = packet[TCP].sport
            tcp_dport = packet[TCP].dport
            print(f"TCP Packet: {ip_src}:{tcp_sport} -> {ip_dst}:{tcp_dport}")

        # Si el paquete tiene una capa UDP
        elif UDP in packet:
            udp_sport = packet[UDP].sport
            udp_dport = packet[UDP].dport
            print(f"UDP Packet: {ip_src}:{udp_sport} -> {ip_dst}:{udp_dport}")

        else:
            print(f"Other IP Packet: {ip_src} -> {ip_dst}")

# Captura paquetes en la interfaz especificada (puedes cambiar 'eth0' por la interfaz de tu red)
sniff(prn=packet_callback, filter="ip", iface="eth0", store=0)
