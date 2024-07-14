from pprint import pprint

# 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los caracteres restantes

# 2. Contar en un diccionario cuanto se repiten
# los caracteres de un string
# 3. Ordenar las llaves de un diccionario
# por el valor que tienen y devolver una lista

# que contiene tuplas [("a", 3), ("b", 2), ("c", 4), ("d"
# 4. de un listado de tuplas, devolver las tuplas
# que tengan el mayor valor.
# [("a", 3), ("b", 2), ("c", 4)] →> [("c", 4) ]
# 5. Crear un mensaje que diga:
# Los caracteres que más se repiten coh 4 repeticiones son:
# - C
# — D

# - 1


def eliminar_espacios_join(lista):
    lista_sin_espacios = []
    for cadena in lista:
        cadena_sin_espacios = "".join(
            [caracter for caracter in cadena if caracter != " "])
        lista_sin_espacios.append(cadena_sin_espacios)
    return lista_sin_espacios


lista_de_compras = ["manzanas y peras",
                    "plátanos y kiwis", "leche y chocolate", "pan"]

lista_sin_espacios = eliminar_espacios_join(lista_de_compras)
pprint(lista_sin_espacios)


lista_de_compras = ["manzanas y peras",
                    "plátanos y kiwis", "leche y chocolate", "pan"]


def contar_frecuencia_caracteres(lista):
    diccionario_frecuencias = {}
    for cadena in lista:
        for caracter in cadena.lower():  # Convertir a minúsculas
            if caracter in diccionario_frecuencias:
                diccionario_frecuencias[caracter] += 1
            else:
                diccionario_frecuencias[caracter] = 1
    return diccionario_frecuencias


lista_de_compras = ["manzanas y peras",
                    "plátanos y kiwis", "leche y chocolate", "pan"]

diccionario_frecuencias = contar_frecuencia_caracteres(lista_de_compras)
pprint(diccionario_frecuencias)
