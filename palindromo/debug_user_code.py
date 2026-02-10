
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
    list_caracteres = ['á', 'é', 'í', 'ó', 'ú']
    for i in list_caracteres:
        cadena = cadena.replace(i, 'a')
    return cadena

def remplazar_signos(cadena):
    list_signos = ["'", ",", ".", ":", ";", "!", "?"]
    for i in list_signos:
        cadena = cadena.replace(i, '')
    return cadena

# Test assertions
print(f"Testing 'Logró gol': Expected True")
result = es_palindromo("Logró gol")
print(f"Result: {result}")

print(f"Testing 'Dábale arroz a la zorra el abad': Expected True")
result2 = es_palindromo("Dábale arroz a la zorra el abad")
print(f"Result: {result2}")

# Debugging internal state
val = "Logró gol".lower().replace(" ", "")
val = remplazar_caracteres(val)
print(f"Transformed 'Logró gol' internal: {val}")
