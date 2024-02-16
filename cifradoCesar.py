def cifrar_cesar(mensaje, clave, modulo):
    resultado = ""

    for char in mensaje:
        if char.isalpha():
            es_mayuscula = char.isupper()
            char = char.lower()

            cifrado = chr((ord(char) - ord('a') + clave) % modulo + ord('a'))

            if es_mayuscula:
                cifrado = cifrado.upper()

            resultado += cifrado
        else:
            resultado += char

    return resultado


def descifrar_cesar(mensaje_cifrado, clave, modulo):
    resultado = ""

    for char in mensaje_cifrado:
        if char.isalpha():
            es_mayuscula = char.isupper()
            char = char.lower()

            descifrado = chr((ord(char) - ord('a') - clave) % modulo + ord('a'))

            if es_mayuscula:
                descifrado = descifrado.upper()

            resultado += descifrado
        else:
            resultado += char

    return resultado
