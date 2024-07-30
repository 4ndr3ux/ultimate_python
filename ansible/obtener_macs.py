import subprocess
import re

# Lista de IPs
ips = [
    "192.168.0.55",
    "192.168.0.57",
    "192.168.0.58",
    "192.168.0.59",
    "192.168.0.56",
    "192.168.0.60"
]

# Función para obtener la MAC de una IP usando el comando arp
def obtener_mac(ip):
    try:
        # Ejecutar el comando arp para obtener la MAC
        resultado = subprocess.check_output(['arp', '-n', ip]).decode('utf-8')
        # Usar expresión regular para encontrar la MAC
        mac = re.search(r'(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})', resultado, re.IGNORECASE).group(0)
        return mac
    except:
        return "No se pudo obtener la MAC para {}".format(ip)

# Iterar sobre cada IP y obtener la MAC
for ip in ips:
    mac = obtener_mac(ip.strip())  # Eliminar cualquier espacio en blanco alrededor de la IP
    print("IP: {}, MAC: {}".format(ip, mac))

