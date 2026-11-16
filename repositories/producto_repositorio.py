"""Acceso a datos de Producto, guardado en un archivo JSON."""

from dataclasses import replace
from typing import Optional

from entities.producto import Producto
from repositories.base import Repositorio


class ProductoRepositorio(Repositorio):
    def crear(self, producto: Producto) -> Producto:
        """Guarda un producto nuevo y le asigna un id unico."""
        nuevo_id = max((int(clave) for clave in self._buffer), default=0) + 1
        nuevo = replace(producto, id=nuevo_id)
        self._buffer[str(nuevo_id)] = nuevo.to_dict()
        self._guardar()
        return nuevo

    def obtener_por_id(self, id_producto: int) -> Optional[Producto]:
        datos = self._buffer.get(str(id_producto))
        return Producto.from_dict(datos) if datos else None

    def obtener_todos(self) -> list[Producto]:
        return [Producto.from_dict(datos) for datos in self._buffer.values()]

    def actualizar(self, producto: Producto) -> Producto:
        self._buffer[str(producto.id)] = producto.to_dict()
        self._guardar()
        return producto

    def eliminar(self, id_producto: int) -> bool:
        if self._buffer.pop(str(id_producto), None) is None:
            return False
        self._guardar()
        return True

    def existe_nombre(self, nombre: str, excluir_id: Optional[int] = None) -> bool:
        nombre = nombre.strip().lower()
        return any(
            datos["nombre"].lower() == nombre and datos["id"] != excluir_id
            for datos in self._buffer.values()
        )
