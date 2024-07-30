#!/bin/bash

# Usuario y contraseña
USER="root"
PASSWORD="fedores7x"

# Arreglo de IPs de los servidores
HOSTS=(
    "192.168.0.55"
    "192.168.0.57"
    "192.168.0.58"
    "192.168.0.59"
    "192.168.0.56"
    "192.168.0.60"
)

# Función para reiniciar un servidor
restart_server() {
    local ip=$1

    sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no $USER@$ip <<EOF
echo $PASSWORD | sudo -S reboot
EOF

    if [ $? -eq 0 ]; then
        echo -e "\e[32mServidor en $ip está reiniciándose...\e[0m"
    else
        echo -e "\e[31mError al intentar reiniciar el servidor en $ip.\e[0m"
    fi
}

# Iterar sobre las IPs para reiniciar cada servidor
for ip in "${HOSTS[@]}"; do
    restart_server $ip
done

