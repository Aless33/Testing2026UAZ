import unittest
from biblioteca import Libro, Usuario, Biblioteca


class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()
        self.libro1 = Libro(1, "La biblia", "Jesus/dios")
        self.usuario1 = Usuario(1, "Alessandro")

    # Registrar libro
    def test_registrar_libro(self):
        self.biblioteca.registrar_libro(self.libro1)
        self.assertIn(self.libro1, self.biblioteca.libros)

    # Buscar libro
    def test_buscar_libro_existente(self):
        self.biblioteca.registrar_libro(self.libro1)
        resultado = self.biblioteca.buscar_libro("La biblia")
        self.assertEqual(resultado, self.libro1)

    # Buscar libro inexistente
    def test_buscar_libro_inexistente(self):
        resultado = self.biblioteca.buscar_libro("La biblia 2")
        self.assertIsNone(resultado)

    # Registrar usuario
    def test_registrar_usuario(self):
        self.biblioteca.registrar_usuario(self.usuario1)
        self.assertIn(self.usuario1, self.biblioteca.usuarios)

    # Prestar libro
    def test_prestar_libro_disponible(self):
        self.biblioteca.registrar_libro(self.libro1)
        self.biblioteca.registrar_usuario(self.usuario1)
        resultado = self.biblioteca.prestar_libro(1, 1)
        self.assertTrue(resultado)
        self.assertFalse(self.libro1.disponible)

    # Prestar libro ya prestado
    def test_prestar_libro_ya_prestado(self):
        self.biblioteca.registrar_libro(self.libro1)
        self.biblioteca.registrar_usuario(self.usuario1)
        self.biblioteca.prestar_libro(1, 1)
        resultado = self.biblioteca.prestar_libro(1, 1)
        self.assertFalse(resultado)

    # Devolver libro
    def test_devolver_libro(self):
        self.biblioteca.registrar_libro(self.libro1)
        self.biblioteca.prestar_libro(1, 1)
        resultado = self.biblioteca.devolver_libro(1)
        self.assertTrue(resultado)

    # Consultar todos
    def test_consultar_todos(self):
        self.biblioteca.registrar_libro(self.libro1)
        self.biblioteca.registrar_usuario(self.usuario1)
        self.assertEqual(len(self.biblioteca.consultar_libros()), 1)
        self.assertEqual(len(self.biblioteca.consultar_usuarios()), 1)

    # Busqueda con mayus/minus mezcladas
    def test_buscar_libro_case_insensitive(self):
        self.biblioteca.registrar_libro(self.libro1)
        resultado = self.biblioteca.buscar_libro("lA BiBLiA")
        self.assertEqual(resultado, self.libro1)

    # Intentar prestar un libro inexistente
    def test_prestar_libro_id_inexistente(self):
        resultado = self.biblioteca.prestar_libro(568, 1)
        self.assertFalse(resultado)

    # Intentar devolver un libro que ya estaba disponible
    def test_devolver_libro_que_no_estaba_prestado(self):
        self.biblioteca.registrar_libro(self.libro1)
        resultado = self.biblioteca.devolver_libro(self.libro1.id)
        self.assertFalse(resultado)
        self.assertTrue(self.libro1.disponible)

    # Intentar devolver un libro que no existe en la biblioteca
    def test_devolver_libro_id_inexistente(self):
        resultado = self.biblioteca.devolver_libro(999)
        self.assertFalse(resultado)

    # Registrar usuario sin nombre
    def test_registrar_usuario_nombre_vacio(self):
        usuario_sin_nombre = Usuario(2, "")
        self.biblioteca.registrar_usuario(usuario_sin_nombre)
        self.assertIn(usuario_sin_nombre, self.biblioteca.usuarios)

    # Id repetido al registrar un usuario
    def test_registrar_usuario_id_duplicado(self):
        usuario_duplicado = Usuario(1, "Pedro")
        self.biblioteca.registrar_usuario(self.usuario1)
        self.biblioteca.registrar_usuario(usuario_duplicado)
        self.assertEqual(len(self.biblioteca.usuarios), 2)

    # Id repetido al registrar un libro
    def test_registrar_libro_id_duplicado(self):
        libro2 = Libro(1, "Duplicado", "Autor")

        self.biblioteca.registrar_libro(self.libro1)
        self.biblioteca.registrar_libro(libro2)

        self.assertEqual(len(self.biblioteca.libros), 2)

    # Id no numerico al registrar un libro
    def test_registrar_libro_id_no_numerico(self):
        with self.assertRaises(ValueError):
            Libro("abc", "Titulo", "Autor")

    # Id no numerico al registrar un usuario
    def test_registrar_usuario_id_no_numerico(self):
        with self.assertRaises(ValueError):
            Usuario("abc", "Nombre")
    
    # Titulo vacio al registrar un libro
    def test_libro_titulo_vacio(self):
        with self.assertRaises(ValueError):
            Libro(10, "", "Autor")
    
    # Autor vacio al registrar un libro
    def test_libro_autor_vacio(self):
        with self.assertRaises(ValueError):
            Libro(10, "Titulo", "")
    
    # Titulo vacio al registrar un usuario
    def test_registrar_usuario_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Usuario(2, "")
                
if __name__ == '__main__':
    unittest.main()
