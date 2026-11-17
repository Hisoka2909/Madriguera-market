"""Entidad Categoria."""

from enum import Enum


class Categoria(str, Enum):
    ACCESORIOS = "Accesorios"
    PELUCHES = "Peluches"
    STICKERS_Y_PINES = "Stickers y pines"
    ARTE_Y_COLECCIONABLES = "Arte y coleccionables"
