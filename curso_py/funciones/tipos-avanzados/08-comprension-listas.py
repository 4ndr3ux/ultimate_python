usuarios = [
    ["Pedro", 4],
    ["Felipe", 1],
    ["Pablo", 5]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

nombres = [i[0] for i in usuarios]
# print(nombres)

# filtro
nombres = [i for i in usuarios if i[1] > 2]
print(nombres)

# filtro y transformar
nombres = [i[0] for i in usuarios if i[1] > 2]


nombres = list(map(lambda i: i[0], usuarios))
print(nombres)

menosUsuarios = list(filter(lambda i: i[1] > 2, usuarios))
print(menosUsuarios)
