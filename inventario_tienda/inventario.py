class Producto:
    def __init__(self, id_prod, nombre, cantidad, precio):
        self.id = id_prod
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = {}

    def registrar_producto(self, id_prod, nombre, cantidad, precio):
        if id_prod in self.productos:
            raise ValueError("ID duplicado")
        self.productos[id_prod] = Producto(id_prod, nombre, cantidad, precio)
        return True

    def obtener_todos(self):
        return list(self.productos.values())

    def buscar_por_nombre(self, nombre):
        for prod in self.productos.values():
            if prod.nombre.lower() == nombre.lower():
                return prod
        return None

    def actualizar_stock(self, id_prod, nueva_cantidad):
        if id_prod not in self.productos:
            raise KeyError("Producto no encontrado")
        self.productos[id_prod].cantidad = nueva_cantidad

    def eliminar_producto(self, id_prod):
        if id_prod in self.productos:
            del self.productos[id_prod]
            return True
        return False

    def registrar_venta(self, id_prod, cantidad):
        prod = self.productos.get(id_prod)
        if not prod:
            raise KeyError("Producto no encontrado")
        if prod.cantidad < cantidad:
            raise ValueError("Stock insuficiente")
        prod.cantidad -= cantidad

    def registrar_compra(self, id_prod, cantidad):
        prod = self.productos.get(id_prod)
        if not prod:
            raise KeyError("Producto no encontrado")
        prod.cantidad += cantidad

    def calcular_valor_total(self):
        return sum(p.cantidad * p.precio for p in self.productos.values())