# set significa grupo o conjunto
primerSet = {1, 1, 2, 2, 3, 4}
print(primerSet)

segundoSet = [3, 4, 5]  # es una lista
segundoSet = set(segundoSet)  # convierte la lista en set
print(segundoSet)

print(primerSet | segundoSet)
print(primerSet & segundoSet)
print(primerSet - segundoSet)
print(primerSet ^ segundoSet)

if 5 in segundoSet:
    print("hola mundo")
