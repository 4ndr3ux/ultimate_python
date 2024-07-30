#!/bin/bash
# Lista de direcciones IP
ips=("192.168.0.55" "192.168.0.57" "192.168.0.58" "192.168.0.59" "192.168.0.56")
# Comando para crear el usuario y configurar sudo
command="useradd andres && echo 'andres ALL=(ALL) NOPASSWD:ALL' | sudo tee /etc/sudoers.d/andres"
# Iterar sobre cada IP
for ip in "${ips[@]}"; do
  echo "Procesando $ip..."
  if ssh root@$ip << EOF
    if id "andres" &>/dev/null; then
      echo "El usuario andres ya existe en $ip"
    else
      $command
      if [ $? -eq 0 ]; then
        echo "Usuario andres creado exitosamente en $ip"
      else
        echo "Error al crear el usuario andres en $ip"
      fi
    fi
    visudo -c
EOF
  then
    echo "Operación completada en $ip"
  else
    echo "Error al conectar o ejecutar comandos en $ip"
  fi
done
