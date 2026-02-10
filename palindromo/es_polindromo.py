def es_palindromo(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace(' ', '')
    cadena = remplazar_caracteres(cadena)
    cadena = remplazar_signos(cadena)  
    for i in range(len(cadena)):
        if cadena[i] != cadena[len(cadena) - i - 1]:
            return False
    return True

def remplazar_caracteres(cadena):
    reemplazos = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u'
    }
    for acento, normal in reemplazos.items():
        cadena = cadena.replace(acento, normal)
    return cadena

def remplazar_signos(cadena):
    list_signos = ["'", ",", ".", ":", ";", "!", "?"]
    for i in list_signos:
        cadena = cadena.replace(i, '')
    return cadena



