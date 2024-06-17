#!/bin/bash
#cd /home/andres/Documents/cursos/ultimate_python
#git pull origin main
#git add .
#git commit -m "$"
#git push origin main



# Solicitar el mensaje del commit al usuario
echo "Introduce el mensaje del commit: "
read commit_message

# Actualizar el repositorio
git pull origin main

# Añadir todos los cambios
git add .

# Hacer commit con el mensaje proporcionado por el usuario
git commit -m "$commit_message"

# Enviar los cambios al repositorio remoto
git push origin main