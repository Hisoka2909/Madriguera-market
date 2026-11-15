"""Entidad Usuario de Madriguera Market (contenido apto para todo publico UwU)."""

from dataclasses import dataclass, field
from datetime import date
from typing import Optional

from entities.excepciones import ErrorValidacion


@dataclass
class Pedido:
    id: str
    id_usuario: int
    carrito: dict
    estado: str

    def __post_init__(self):
        if not self.estado:
            raise ErrorValidacion("El estado es obligatorio")
        if len(self.nombre) > 100:
            raise ErrorValidacion("El estado no puede superar los 15 caracteres OnO")
        if len(self.direccion) > 100:
            raise ErrorValidacion(
                "La dirección no puede superar los 100 caracteres OnO"
            )
        if self.id_usuario is not None and self.id <= 0:
            raise ErrorValidacion("El ID de usuario debe ser un entero positivo OnO")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "carrito": self.carrito,
            "estado": self.estado,
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Pedido":
        return cls(
            id=datos.get("id"),
            id_usuario=datos.get("id_usuario"),
            carrito=datos.get("carrito"),
            estado=datos.get("estado"),
        )
