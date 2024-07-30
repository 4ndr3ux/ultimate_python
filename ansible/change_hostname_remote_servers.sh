#!/bin/bash

# Usuario y contraseña
USER="root"
PASSWORD="fedores7"

# Arreglo de hostnames e IPs
declare -A HOSTS
HOSTS=(
    [web1]="192.168.0.55"
    [web2]="192.168.0.57"
    [LB1]="192.168.0.58"
    [DB1]="192.168.0.59"
    [BACKUP1]="192.168.0.56"
    [MON01]="192.168.0.60"
)

# Función para cambiar el hostname
change_hostname() {
    local new_hostname=$1
    local ip=$2

    # Comando para cambiar el hostname de forma remota
    sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no $USER@$ip "echo $PASSWORD | sudo -S hostnamectl set-hostname $new_hostname"
}

# Función para mostrar el resultado
show_result() {
    local new_hostname=$1
    local ip=$2

    # Verificar el cambio de hostname
    sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no $USER@$ip "hostname" | grep -q $new_hostname
    if [ $? -eq 0 ]; then
        echo -e "\e[32mhostname: $new_hostname, IP: $ip OK\e[0m"
    else
        echo -e "\e[31mhostname: $new_hostname, IP: $ip ERROR\e[0m"
    fi
}

# Iterar sobre los hostnames e IPs para cambiarlos y verificar
for hostname in "${!HOSTS[@]}"; do
    ip=${HOSTS[$hostname]}
    change_hostname $hostname $ip
    show_result $hostname $ip
done

