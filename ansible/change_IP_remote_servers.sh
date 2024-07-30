#!/bin/bash

# Usuario y contraseña
USER="root"
PASSWORD="fedorees7x"

# Arreglo de hostnames e IPs con sus configuraciones
declare -A HOSTS
HOSTS=(
    [web1]="192.168.0.55"
    [web2]="192.168.0.57"
    [LB1]="192.168.0.58"
    [DB1]="192.168.0.59"
    [BACKUP1]="192.168.0.56"
    [MON01]="192.168.0.60"
)

# Mascara de subred, puerta de enlace y DNS
SUBNET_MASK="255.255.255.0"
GATEWAY="192.168.0.1"
DNS="8.8.8.8"

# Función para configurar la IP estática
configure_static_ip() {
    local ip=$1
    local hostname=$2

    # Determinar el nombre de la interfaz de red
    local interface=$(sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no $USER@$ip "nmcli device status | grep ethernet | awk '{print \$1}'")

    # Configurar la IP estática
    sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no $USER@$ip <<EOF
echo $PASSWORD | sudo -S nmcli connection modify \$interface ipv4.addresses $ip/24 ipv4.gateway $GATEWAY ipv4.dns $DNS ipv4.method manual
echo $PASSWORD | sudo -S nmcli connection up \$interface
EOF
}

# Función para mostrar el resultado
show_result() {
    local ip=$1
    local hostname=$2

    # Verificar la configuración de IP
    sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no $USER@$ip "ip addr show" | grep -q $ip
    if [ $? -eq 0 ]; then
        echo -e "\e[32mHostname: $hostname, IP: $ip OK\e[0m"
    else
        echo -e "\e[31mHostname: $hostname, IP: $ip ERROR\e[0m"
    fi
}

# Iterar sobre los hostnames e IPs para configurarlos y verificar
for hostname in "${!HOSTS[@]}"; do
    ip=${HOSTS[$hostname]}
    configure_static_ip $ip $hostname
    show_result $ip $hostname
done

