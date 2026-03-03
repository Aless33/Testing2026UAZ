class Libro:
    def __init__(self, id, titulo, autor):
        if not isinstance(id, int):
            raise ValueError("El ID del libro debe ser numerico")

        if not titulo.strip():
            raise ValueError("El titulo no puede estar vacio")

        if not autor.strip():
            raise ValueError("El autor no puede estar vacio")

        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __eq__(self, other):
        if not isinstance(other, Libro):
            return False
        return self.id == other.id


class Usuario:
    def __init__(self, id, nombre):
        if not isinstance(id, int):
            raise ValueError("El ID del usuario debe ser numerico")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacio")

        self.id = id
        self.nombre = nombre

    def __eq__(self, other):
        if not isinstance(other, Usuario):
            return False
        return self.id == other.id


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    # Registrar libro
    def registrar_libro(self, libro):
        self.libros.append(libro)

    # Buscar libro por título (case insensitive)
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    # Registrar usuario
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    # Prestar libro
    def prestar_libro(self, libro_id, usuario_id):
        libro = self._buscar_libro_por_id(libro_id)

        if libro and libro.disponible:
            libro.disponible = False
            return True

        return False

    # Devolver libro
    def devolver_libro(self, libro_id):
        libro = self._buscar_libro_por_id(libro_id)

        if libro and not libro.disponible:
            libro.disponible = True
            return True

        return False

    # Consultar libros
    def consultar_libros(self):
        return self.libros

    # Consultar usuarios
    def consultar_usuarios(self):
        return self.usuarios

    # Métodos privados auxiliares
    def _buscar_libro_por_id(self, libro_id):
        for libro in self.libros:
            if libro.id == libro_id:
                return libro
        return None

    def _buscar_libo_por_id_seguro(self, libro_id):
        for libro in self.libros:
            if libro.id == libro_id:
                return libro
        return None

    def _buscar_usuario_por_id(self, usuario_id):
        for usuario in self.usuarios:
            if usuario.id == usuario_id:
                return usuario
        return None


def mostrar_menu():
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Buscar libro")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Ver libros")
    print("7. Ver usuarios")
    print("0. Salir")


def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            id = int(input("ID del libro: "))
            titulo = input("Título: ")
            autor = input("Autor: ")
            libro = Libro(id, titulo, autor)
            biblioteca.registrar_libro(libro)
            print("Libro registrado")

        elif opcion == "2":
            id = int(input("ID del usuario: "))
            nombre = input("Nombre: ")
            usuario = Usuario(id, nombre)
            biblioteca.registrar_usuario(usuario)
            print("Usuario registrado")

        elif opcion == "3":
            titulo = input("Título a buscar: ")
            libro = biblioteca.buscar_libro(titulo)
            if libro:
                estado = "Disponible" if libro.disponible else "Prestado"
                print(f"{libro.titulo} - {libro.autor} ({estado})")
            else:
                print("Libro no encontrado")

        elif opcion == "4":
            libro_id = int(input("ID del libro: "))
            usuario_id = int(input("ID del usuario: "))
            if biblioteca.prestar_libro(libro_id, usuario_id):
                print("Libro prestado")
            else:
                print("No se pudo prestar el libro")

        elif opcion == "5":
            libro_id = int(input("ID del libro: "))
            if biblioteca.devolver_libro(libro_id):
                print("Libro devuelto.")
            else:
                print("No se pudo devolver el libro")

        elif opcion == "6":
            libros = biblioteca.consultar_libros()
            if not libros:
                print("No hay libros registrados")
            for libro in libros:
                estado = "Disponible" if libro.disponible else "Prestado"
                print(f"{libro.id} - {libro.titulo} - {libro.autor} ({estado})")

        elif opcion == "7":
            usuarios = biblioteca.consultar_usuarios()
            if not usuarios:
                print("No hay usuarios registrados")
            for usuario in usuarios:
                print(f"{usuario.id} - {usuario.nombre}")

        elif opcion == "0":
            break

        else:
            print("Opción invalida.")


if __name__ == "__main__":
    main()

    unittest.main()
