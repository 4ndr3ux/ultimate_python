lista = [1, 2, 3, 4]
listaTupla = (1, 2, 3, 4)

lista2 = [5, 6]
# print(1, 2, 3, 4)
print(*lista)
print(*listaTupla)

listaCombinada = [*lista, *lista2]
print(listaCombinada)

punto1 = {"x": 19}
punto2 = {"y": 15}

nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)
