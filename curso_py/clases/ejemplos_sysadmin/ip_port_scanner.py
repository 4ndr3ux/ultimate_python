import socket


class PortScanner:
    def __init__(self, target_ip):
        self.target_ip = target_ip

    def scan_port(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((self.target_ip, port))
        if result == 0:
            print(f"Puerto {port} está abierto.")
        else:
            print(f"Puerto {port} está cerrado.")
        sock.close()

    def scan_ports(self, start_port, end_port):
        for port in range(start_port, end_port + 1):
            self.scan_port(port)


# Uso de la clase
ip = input("ingrese la IP para escanear: ")
scanner = PortScanner(ip)
scanner.scan_ports(20, 100)
