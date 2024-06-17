print("Bienvenido a CALCULADORA, tipar fin para terminar: ")

num1 = int(input("Ingrese un numero para operar: "))
num2 = int(input("Ingrese Otro numero para operar: "))

print("1. SUMA")
print("2. RESTA")
print("3. Multiplo")
print("4. Division")

operacion = int(input("Selecciones el numero de la operacion a Realizar: "))


def fun_caclculadora(operacion, num1, num2):
    if operacion == 1:
        return num1 + num2
    elif operacion == 2:
        return num1 - num2
    elif operacion == 3:
        return num1 * num2
    elif operacion == 4:
        return num1 / num2
    else:
        return None


# Llamar a la función resultado con los argumentos correctos
resultado_operacion = fun_caclculadora(operacion, num1, num2)

if resultado_operacion is not None:
    print(f"El resultado de la operación es: {resultado_operacion}")
else:
    print("Operación inválida.")
