#!/bin/bash

# Lista de direcciones IP de los servidores
ips=("192.168.0.55" "192.168.0.57" "192.168.0.58" "192.168.0.59" "192.168.0.56")

# Comando a ejecutar en cada servidor
command="usermod -aG wheel andres && echo 'andres ALL=(ALL) NOPASSWD:ALL' | sudo tee -a /etc/sudoers"

# Iterar sobre cada IP y ejecutar el comando de forma remota
for ip in "${ips[@]}"; do
  ssh root@$ip <<EOF
    $command
    visudo -c
  EOF
  if [ $? -eq 0 ]; then
    echo "Comando ejecutado correctamente en $ip"
  else
    echo "Error al ejecutar el comando en $ip"
  fi
done

