def calcular_precio_total(productos):
    subtotal = 0
    productos_vistos = [] 
    
    for producto in productos:
        nombre_producto = producto["Nombre"].lower()
        

        resultado_duplicado = verificar_duplicados(nombre_producto, productos_vistos)
        if resultado_duplicado != True:
            return resultado_duplicado
        
        resultado_val = validar_productos(producto)
        if resultado_val != True:
            return resultado_val
            
        precio = producto["precio"] * producto["cantidad"]
        descuento = aplicar_descuento_producto(precio)
        subtotal += precio - descuento
        
    descuento_total = aplicar_descuento_total(subtotal)
    return calcular_total(subtotal, descuento_total)

def aplicar_descuento_producto(precio):
    if precio > 1000:
        return precio * 0.10
    else:
        return 0

def aplicar_descuento_total(subtotal):
    if subtotal > 5000:
        return subtotal * 0.05
    else:
        return 0

def calcular_total(subtotal, descuento):
    return subtotal - descuento

def validar_productos(producto):
    if producto["precio"] <= 0 or producto["cantidad"] <= 0:
        return "Error: Precio o cantidad invalida"
    elif producto["Nombre"] == "":
        return "Error: Nombre invalido"
    return True

def verificar_duplicados(producto_actual, lista_vistos):

    if producto_actual in lista_vistos:
        return "Error: Producto duplicado"
    
    lista_vistos.append(producto_actual)
    return True

