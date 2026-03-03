import unittest
from tareas import GestorTareas


class TestGestorTareas(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorTareas()

    def test_agregar_tarea(self):
        tarea = self.gestor.agregar_tarea("Estudiar", "Repasar unittest")

        self.assertEqual(tarea["id"], 1)
        self.assertEqual(tarea["nombre"], "Estudiar")
        self.assertEqual(tarea["descripcion"], "Repasar unittest")
        self.assertEqual(tarea["estado"], "pendiente")
        self.assertEqual(len(self.gestor.tareas), 1)

    def test_marcar_completada(self):
        tarea = self.gestor.agregar_tarea("Proyecto", "Terminar código")
        self.gestor.marcar_completada(tarea["id"])

        self.assertEqual(self.gestor.tareas[0]["estado"], "completada")

    def test_eliminar_tarea(self):
        tarea = self.gestor.agregar_tarea("Leer", "Leer documentación")
        self.gestor.eliminar_tarea(tarea["id"])

        self.assertEqual(len(self.gestor.tareas), 0)

    def test_eliminar_tarea_inexistente(self):
        with self.assertRaises(ValueError):
            self.gestor.eliminar_tarea(999)

    def test_marcar_tarea_inexistente(self):
        with self.assertRaises(ValueError):
            self.gestor.marcar_completada(888)

    
if __name__ == "__main__":
    unittest.main()