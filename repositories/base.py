"""Base abstracta para los repositorios que guardan sus datos en un archivo JSON."""

import json
import os
from abc import ABC, abstractmethod


class Repositorio(ABC):
    def __init__(self, ruta_archivo: str):
        self.ruta_archivo = ruta_archivo
        self._buffer: dict[str, dict] = self._cargar()

    def _cargar(self) -> dict[str, dict]:
        if not os.path.exists(self.ruta_archivo):
            return {}
        with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
        return json.loads(contenido) if contenido else {}

    def _guardar(self) -> None:
        carpeta = os.path.dirname(self.ruta_archivo)
        if carpeta:
            os.makedirs(carpeta, exist_ok=True)
        with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(self._buffer, archivo, indent=4, ensure_ascii=False)

    @abstractmethod
    def crear(self, entidad):
        """Guarda una entidad nueva."""

    @abstractmethod
    def obtener_por_id(self, id_entidad: int):
        """Busca una entidad por su id."""

    @abstractmethod
    def obtener_todos(self):
        """Devuelve todas las entidades."""

    @abstractmethod
    def actualizar(self, entidad):
        """Reemplaza los datos de una entidad existente."""

    @abstractmethod
    def eliminar(self, id_entidad: int):
        """Elimina una entidad."""
