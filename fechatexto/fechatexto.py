def fecha_texto(fecha):
    if not validar_formato(fecha):
        return "Error de formato"
    partes = fecha.split('/')
    dia = int(partes[0])
    mes = int(partes[1])
    anio = int(partes[2])

    if validar_fecha(dia, mes, anio) == True:
        return f"{escribir_dia(dia)} de {escribir_mes(mes)} de {escribir_mil(anio)}"
    else:
        return validar_fecha(dia, mes, anio)

def validar_fecha(dia, mes, anio):
    if aniobisiesto(anio):
        if mes == 2 and dia > 29: return "La fecha no existe"
    if dia < 1 or dia > 31: return "El dia solo puede ser menor a 31"
    if mes < 1 or mes > 12: return "El mes solo puede ser menor a 12"
    if anio < 1 or anio > 9999: return "El año solo puede ser menor a 9999"
    return True

def aniobisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def escribir_unidades(unidad):
    lista_unidades = ["Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve"]
    if 1 <= unidad <= 9:
        return lista_unidades[unidad - 1]
    return ""

def escribir_decenas(n):
    if n < 10: return escribir_unidades(n).lower()
    
    lista_especiales = ["diez", "once", "doce", "trece", "catorce", "quince", 
                       "dieciseis", "diecisiete", "dieciocho", "diecinueve"]
    if 10 <= n <= 19:
        return lista_especiales[n - 10]
    
    lista_decenas = ["veinte", "treinta", "cuarenta", "cincuenta", "sesenta", 
                    "setenta", "ochenta", "noventa"]
    
    indice_decena = (n // 10) - 2   
    if n % 10 == 0:
        return lista_decenas[indice_decena]
    else:
        return lista_decenas[indice_decena] + " y " + escribir_unidades(n % 10).lower()

def escribir_centenas(n):
    if n == 100: return "cien"
    if n < 100: return escribir_decenas(n)
    
    lista_centenas = ["ciento", "doscientos", "trescientos", "cuatrocientos", 
                     "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
    
    indice_centena = (n // 100) - 1
    resto = n % 100
    
    if resto == 0:
        return lista_centenas[indice_centena]
    else:
        return lista_centenas[indice_centena] + " " + escribir_decenas(resto)

def escribir_mil(n):
    if n < 1000: return escribir_centenas(n)
    if n == 1000: return "mil"
    
    miles = n // 1000
    resto = n % 1000
    
    prefijo = ""
    if miles == 1:
        prefijo = "mil"
    else:
        prefijo = escribir_unidades(miles).lower() + " mil"
        
    if resto == 0:
        return prefijo
    else:
        return prefijo + " " + escribir_centenas(resto)

def escribir_dia(dia):
    return escribir_decenas(dia).capitalize()

def escribir_mes(mes):
    lista_meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                  "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    return lista_meses[mes - 1]

def validar_formato(fecha):
    if not isinstance(fecha, str):
        return False
    partes = fecha.split('/')
    try:
        dia = int(partes[0])
        mes = int(partes[1])
        anio = int(partes[2])
    except ValueError:
        return False
    if len(partes) != 3:
        return False
    return True