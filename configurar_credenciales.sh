#!/bin/bash

# Configurar el almacenamiento de credenciales para Git
git config --global credential.helper store

# Guardar las credenciales en el archivo de configuración de Git
# Reemplaza 'lianone@gmail.com' y 'xxxss588ss' con tu usuario y token
echo "https://lianone@gmail.com:xxxss588ss@github.com" > ~/.git-credentials

echo "Credenciales guardadas en ~/.git-credentials"



