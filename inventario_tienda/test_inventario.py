import unittest
from inventario import Inventario, Producto

class TestInventario(unittest.TestCase):
    def setUp(self):
        self.inventario = Inventario()

    def test_registrar_producto_exito(self):
        # RF1: Registrar producto
        res = self.inventario.registrar_producto(1, "Teclado", 10, 25.0)
        self.assertTrue(res)
        self.assertEqual(len(self.inventario.obtener_todos()), 1)

    def test_registrar_producto_duplicado_error(self):
        # Caso de prueba: ID duplicado
        self.inventario.registrar_producto(1, "Teclado", 10, 25.0)
        with self.assertRaises(ValueError):
            self.inventario.registrar_producto(1, "Mouse", 5, 10.0)

    def test_buscar_producto_por_nombre(self):
        # RF2: Buscar producto por nombre
        self.inventario.registrar_producto(1, "Teclado", 10, 25.0)
        prod = self.inventario.buscar_por_nombre("Teclado")
        self.assertIsNotNone(prod)
        self.assertEqual(prod.nombre, "Teclado")

    def test_eliminar_producto(self):
        # RF3: Eliminar producto
        self.inventario.registrar_producto(1, "Teclado", 10, 25.0)
        self.inventario.eliminar_producto(1)
        self.assertEqual(len(self.inventario.obtener_todos()), 0)

    def test_actualizar_stock(self):
        # RF4: Actualizar stock
        self.inventario.registrar_producto(1, "Teclado", 10, 25.0)
        self.inventario.actualizar_stock(1, 5)
        self.assertEqual(self.inventario.productos[1].cantidad, 5)

    def test_registrar_venta(self):
        # RF5: Registrar venta
        self.inventario.registrar_producto(1, "Teclado", 10, 25.0)
        self.inventario.registrar_venta(1, 2)
        self.assertEqual(self.inventario.productos[1].cantidad, 8)

    def test_registrar_compra(self):
        # RF6: Registrar compra
        self.inventario.registrar_producto(1, "Teclado", 10, 25.0)
        self.inventario.registrar_compra(1, 5)
        self.assertEqual(self.inventario.productos[1].cantidad, 15)

    def test_calcular_valor_total(self):
        # RF7: Calcular valor total
        self.inventario.registrar_producto(1, "Teclado", 10, 25.0)
        self.inventario.registrar_producto(2, "Mouse", 5, 10.0)
        self.assertEqual(self.inventario.calcular_valor_total(), 275.0)

    def test_buscar_producto_case_insensitive(self):
        # RF3: Buscar sin importar mayúsculas
        self.inv.registrar_producto(10, "Monitor Gaming", 2, 300.0)
        encontrado = self.inv.buscar_por_nombre("monitor gaming")
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.id, 10)

    def test_venta_stock_exacto(self):
        # RF6 & RF8: Vender todo lo que hay
        self.inv.registrar_producto(20, "Mouse", 1, 15.0)
        self.inv.registrar_venta(20, 1)
        self.assertEqual(self.inv.productos[20].cantidad, 0)

    def test_eliminar_inexistente_retorna_falso(self):
        # RF5: Eliminar algo que no existe
        resultado = self.inv.eliminar_producto(999)
        self.assertFalse(resultado)

    def test_compra_producto_inexistente_error(self):
        # RF7: Reabastecer algo que no está registrado
        with self.assertRaises(KeyError):
            self.inv.registrar_compra(555, 10)

    def test_actualizar_stock_a_cero(self):
        # RF4: Actualizar stock manualmente
        self.inv.actualizar_stock(1, 0)
        self.assertEqual(self.inv.productos[1].cantidad, 0)