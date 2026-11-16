"""Entidad Producto de Madriguera Market (contenido apto para todo publico)"""

from dataclasses import dataclass, field
from datetime import date
from typing import Optional

from entities.categoria import Categoria
from entities.excepciones import ErrorValidacion


@dataclass
class Producto:
    nombre: str
    descripcion: str
    precio: float
    cantidad: int
    categoria: Categoria
    id: Optional[int] = None 
    stock_minimo: int = 5
    fecha_ingreso: date = field(default_factory=date.today)

    def __post_init__(self):
        self.nombre = (self.nombre or "").strip()
        self.descripcion = (self.descripcion or "").strip()

        if not self.nombre:
            raise ErrorValidacion("El nombre es obligatorio.")
        if len(self.nombre) > 100:
            raise ErrorValidacion("El nombre no puede superar 100 caracteres.")
        if len(self.descripcion) > 300:
            raise ErrorValidacion("La descripcion no puede superar 300 caracteres.")
        if isinstance(self.precio, bool) or not isinstance(self.precio, (int, float)):
            raise ErrorValidacion("El precio debe ser un numero.")
        if self.precio <= 0:
            raise ErrorValidacion("El precio debe ser mayor que cero.")
        if isinstance(self.cantidad, bool) or not isinstance(self.cantidad, int):
            raise ErrorValidacion("La cantidad debe ser un entero.")
        if self.cantidad < 0:
            raise ErrorValidacion("La cantidad no puede ser negativa.")
        if self.stock_minimo < 0:
            raise ErrorValidacion("El stock minimo no puede ser negativo.")
        if self.id is not None and self.id <= 0:
            raise ErrorValidacion("El id debe ser un entero positivo.")

        try:
            self.categoria = Categoria(self.categoria)
        except ValueError as exc:
            validas = ", ".join(c.value for c in Categoria)
            raise ErrorValidacion(f"Categoria invalida. Opciones: {validas}.") from exc

    def esta_por_agotarse(self) -> bool:
        return self.cantidad <= self.stock_minimo

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "categoria": self.categoria.value,
            "stock_minimo": self.stock_minimo,
            "fecha_ingreso": self.fecha_ingreso.isoformat(),
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Producto":
        fecha = datos.get("fecha_ingreso")
        if isinstance(fecha, str):
            fecha = date.fromisoformat(fecha)
        return cls(
            id=datos.get("id"),
            nombre=datos.get("nombre"),
            descripcion=datos.get("descripcion", ""),
            precio=datos.get("precio"),
            cantidad=datos.get("cantidad"),
            categoria=datos.get("categoria"),
            stock_minimo=datos.get("stock_minimo", 5),
            fecha_ingreso=fecha or date.today(),
        )
