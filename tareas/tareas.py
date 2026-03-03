class GestorTareas:
    def __init__(self):
        """Inicializa una lista vacía de tareas."""
        self.tareas = []
        self.contador_id = 1  

    def agregar_tarea(self, nombre, descripcion):
        """Agrega una nueva tarea."""
        if not nombre or not descripcion:
            raise ValueError("El nombre y la descripción no pueden estar vacíos.")

        tarea = {
            "id": self.contador_id,
            "nombre": nombre,
            "descripcion": descripcion,
            "estado": "pendiente"
        }

        self.tareas.append(tarea)
        self.contador_id += 1
        return tarea

    def marcar_completada(self, tarea_id):
        """Marca una tarea como completada."""
        tarea = self._buscar_tarea(tarea_id)
        tarea["estado"] = "completada"

    def eliminar_tarea(self, tarea_id):
        """Elimina una tarea por ID."""
        tarea = self._buscar_tarea(tarea_id)
        self.tareas.remove(tarea)

    def obtener_tareas_por_estado(self, estado):
        """Retorna todas las tareas en un estado específico."""
        estados_validos = ["pendiente", "en progreso", "completada"]
        if estado not in estados_validos:
            raise ValueError(f"Estado inválido. Estados válidos: {estados_validos}")

        return [t for t in self.tareas if t["estado"] == estado]

    def _buscar_tarea(self, tarea_id):
        """Busca una tarea por ID o lanza error si no existe."""
        for tarea in self.tareas:
            if tarea["id"] == tarea_id:
                return tarea
        raise ValueError(f"No existe una tarea con ID {tarea_id}")