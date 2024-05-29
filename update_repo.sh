#!/bin/bash
cd /home/andres/Documents/cursos_python/ultimate_python
git pull origin main
git add .
git commit -m "$1"
git push origin main

