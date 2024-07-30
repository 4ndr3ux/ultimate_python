#!/bin/bash

# Define la lista de servidores y sus direcciones IP
declare -A servers=(
  ["web1"]="192.168.0.55"
  ["web2"]="192.168.0.57"
  ["LB1"]="192.168.0.58"
  ["DB1"]="192.168.0.59"
  ["BACKUP1"]="192.168.0.56"
  ["MON01"]="192.168.0.60"
)

# Define el usuario remoto
REMOTE_USER="andres"

# Comando para agregar al usuario andres al grupo sudo y configurar sudo sin contraseña
SUDOERS_ENTRY="andres ALL=(ALL) NOPASSWD:ALL"
COMMAND="echo '$SUDOERS_ENTRY' | sudo tee /etc/sudoers.d/andres && sudo usermod -aG sudo $REMOTE_USER"

# Loop para iterar sobre cada servidor e IP
for server in "${!servers[@]}"; do
  IP="${servers[$server]}"
  
  echo "Configuring $server ($IP)..."
  
  # Ejecuta el comando de forma remota usando SSH
  ssh -o StrictHostKeyChecking=no "$REMOTE_USER@$IP" "$COMMAND"
  
  if [ $? -eq 0 ]; then
    echo -e "$server ($IP): \e[32mOK\e[0m"
  else
    echo -e "$server ($IP): \e[31mFAILED\e[0m"
  fi
done

