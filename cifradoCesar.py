alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚabcdefghijklmnopqrstuvwxyzáéíóú"
modulo = len(alfabeto)

def cifrar_cesar(mensaje, clave):
    """
    #2
    """
    resultado = ""
    for char in mensaje:
        if char in alfabeto:
            indice = alfabeto.index(char)
            indice_cifrado = (indice + clave) % modulo
            resultado += alfabeto[indice_cifrado]
        else:
            resultado += char
    return resultado

def descifrar_cesar(mensaje_cifrado, clave):
    """
    #3
    """
    resultado = ""
    for char in mensaje_cifrado:
        if char in alfabeto:
            indice = alfabeto.index(char)
            indice_descifrado = (indice - clave) % modulo
            resultado += alfabeto[indice_descifrado]
        else:
            resultado += char
    return resultado