min_edad = 25
limite_edad = 65

edad = int(
    input("Ingrese la edad de la persona que quiere ingresar a la Piscina: "))

if edad >= min_edad and edad <= limite_edad:
    print("puede entrar a la piscina..")
else:
    print("No puede1 entrar a la piscina..")
