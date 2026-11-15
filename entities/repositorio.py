import json
import os
from abc import ABC, abstractmethod
from usuario import Usuario
from producto import Producto
from pedido import Pedido


class Repositorio(ABC):

    def __init__(self, ruta_archivo: str):
        self.ruta_archivo = ruta_archivo
        self._buffer: dict[str, dict] = self._cargar()

    def _cargar(self) -> dict[str, dict]:
        if not os.path.exists(self.ruta_archivo):
            return {}
        with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    def _guardar(self) -> None:
        with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(self._buffer, archivo, indent=4, ensure_ascii=False)

    @abstractmethod
    def crear(self, entidad):
        pass

    @abstractmethod
    def obtener_por_id(self, id: int):
        pass

    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def actualizar(self, entidad):
        pass

    @abstractmethod
    def eliminar(self, id: int) -> None:
        pass


class RepositorioUsuario(Repositorio):

    def crear(self, entidad: Usuario) -> Usuario:
        clave = str(entidad.id)
        if clave in self._buffer:
            raise ValueError(f"Ya existe un usuario con ese ID TwT: {entidad.id}")

        for claves in self._buffer:
            claves = str(claves)
            reg = self._buffer[claves]
            if reg["email"] == entidad.email:
                raise ValueError(
                    f"Ya existe un usuario con ese email TwT: {entidad.email}"
                )
            if reg["documento"] == entidad.documento:
                raise ValueError(
                    f"Ya existe un usuario con ese documento TwT: {entidad.documento}"
                )

        self._buffer[clave] = entidad.to_dict()
        self._guardar()
        return entidad

    def obtener_por_id(self, id: int) -> Usuario:
        clave = str(id)
        if clave not in self._buffer:
            raise KeyError(f"No existe ningún registro con el ID {id}. >n<")

        return Usuario.from_dict(self._buffer[clave])

    def obtener_todos(self) -> list[Usuario]:
        return [Usuario(**datos) for datos in self._buffer.values()]

    def actualizar(self, entidad: Usuario) -> Usuario:
        clave = str(entidad.id)
        if clave not in self._buffer:
            raise KeyError(
                f"No se puede actualizar el usuario con ID {clave} porque no existe UnU"
            )
        self._buffer[clave] = entidad.to_dict()
        self._guardar()
        return entidad

    def eliminar(self, id: int) -> None:
        clave = str(id)
        if clave not in self._buffer:
            raise KeyError(f"No se encontró el registro, no se puede borrar UnU")
        reg = self._buffer[clave]
        reg["estado"] = "Inactivo"
        self._buffer[clave] = reg
        self._guardar


class RepositorioPedido(Repositorio):

    def crear(self, entidad: Pedido) -> Pedido:
        clave = str(entidad.id)
        if clave in self._buffer:
            raise ValueError(f"Ya existe un pedido con ese ID TwT: {entidad.id}")

        self._buffer[clave] = entidad.to_dict()
        self._guardar()
        return entidad

    def obtener_por_id(self, id: int) -> Pedido:
        clave = str(id)
        if clave not in self._buffer:
            raise KeyError(f"No existe ningún registro con el ID {id}. >n<")

        return Pedido.from_dict(self._buffer[clave])

    def obtener_todos(self) -> list[Pedido]:
        return [Pedido(**datos) for datos in self._buffer.values()]

    def actualizar(self, entidad: Pedido) -> Pedido:
        clave = str(entidad.id)
        if clave not in self._buffer:
            raise KeyError(
                f"No se puede actualizar el pedido con ID {clave} porque no existe UnU"
            )
        self._buffer[clave] = entidad.to_dict()
        self._guardar()
        return entidad

    def eliminar(self, id: int) -> None:
        clave = str(id)
        if clave not in self._buffer:
            raise KeyError(f"No se encontró el registro, no se puede borrar UnU")
        reg = self._buffer[clave]
        reg["estado"] = "Inactivo"
        self._buffer[clave] = reg
        self._guardar
