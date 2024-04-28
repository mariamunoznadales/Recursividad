def remover_acentos(texto):
    """
    Remueve los acentos del texto.

    Parameters:
    texto (str): El texto del cual se quieren remover los acentos.

    Returns:
    str: El texto sin acentos.
    """
    # Diccionario de mapeo de caracteres acentuados a sus equivalentes sin acento
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}
    # Usamos una expresión generadora para recorrer el texto y reemplazar los caracteres acentuados
    return ''.join(acentos.get(caracter, caracter) for caracter in texto)

def es_palindromo(texto):
    """
    Verifica si el texto es un palíndromo después de realizar los pasos de limpieza.

    Parameters:
    texto (str): El texto a verificar como palíndromo.

    Returns:
    bool: True si el texto es un palíndromo después de los pasos de limpieza, False en caso contrario.
    """
    # Filtrar caracteres alfanuméricos y convertir a minúsculas
    texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
    
    # Remover acentos
    texto_sin_acentos = remover_acentos(texto)
    
    # Verificar si el texto es igual a su imagen reflejada
    return texto_sin_acentos == texto_sin_acentos[::-1]

# Ejemplos
print(es_palindromo("Dábale arroz a la zorra el abad"))  # True
print(es_palindromo("Logré ver gol"))                    # True
print(es_palindromo("Salas"))                            # True
print(es_palindromo("1754571"))                          # True
print(es_palindromo("10000000000000000001"))             # True
print(es_palindromo("Oso"))                              # True
print(es_palindromo("Ejercicio resuelto 6: reconocer un palíndromo"))  # False
