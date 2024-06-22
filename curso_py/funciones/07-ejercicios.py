def es_palindromo(texto):
    texto_sin_espacios = texto.lower().replace(" ", "").rstrip()
    texto_sin_espacios_invertido = texto_sin_espacios[::-1]

    if texto_sin_espacios == texto_sin_espacios_invertido:
        resultado = True
    else:
        resultado = False

    return resultado


# Ejemplos de uso
print("Abba:", es_palindromo("Abba"))  # True
print("Reconocer:", es_palindromo("Reconocer"))  # True
print("Amo la paloma:", es_palindromo("Amo la paloma"))  # True
print("Hola Mundo:", es_palindromo("Hola Mundo"))  # False
print("menem menem menem :", es_palindromo(
    "menem   menem  menem  "))  # True
