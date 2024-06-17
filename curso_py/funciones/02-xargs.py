def func_suma(*numeros):
    resultado = 0
    for i in numeros:
        resultado += i
    print(resultado)


func_suma(2, 5, 9, 10, 15, 41)
