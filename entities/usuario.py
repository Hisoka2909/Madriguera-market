"""Entidad Usuario de Madriguera Market (contenido apto para todo publico UwU)."""

from dataclasses import dataclass
from typing import Optional

from entities.excepciones import ErrorValidacion


@dataclass
class Usuario:
    id: int
    nombre: str
    email: str
    documento: str
    telefono: str
    direccion: str
    estado: str

    def __post__init__(self):
        self.nombre = (self.nombre or "").strip()
        self.direccion = (self.direccion or "").strip()

        if not self.nombre:
            raise ErrorValidacion("El nombre es obligatorio")
        if len(self.nombre) > 100:
            raise ErrorValidacion("El nombre no puede superar los 100 caracteres OnO")
        if len(self.documento) > 16:
            raise ErrorValidacion("El documento no puede superar los 16 caracteres OnO")
        if len(self.telefono) > 20:
            raise ErrorValidacion("El telefono no puede superar los 20 caracteres OnO")
        if len(self.direccion) > 100:
            raise ErrorValidacion(
                "La dirección no puede superar los 100 caracteres OnO"
            )
        if self.id is not None and self.id <= 0:
            raise ErrorValidacion("El ID debe ser un entero positivo")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "documento": self.documento,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "estado": self.estado,
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Usuario":
        return cls(
            id=datos.get("id"),
            nombre=datos.get("nombre"),
            email=datos.get("email"),
            documento=datos.get("documento"),
            telefono=datos.get("telefono"),
            direccion=datos.get("direccion", ""),
            estado=datos.get("estado"),
        )
