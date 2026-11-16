"""Excepciones compartidas por todo el proyecto"""


class ErrorValidacion(ValueError):
    """Se lanza cuando los datos de una entidad no son validos"""
class ProductoNoEncontrado(LookupError):
    """Se lanza cuando se busca un producto que no existe."""
class ProductoDuplicado(ValueError):
    """Se lanza cuando ya existe un producto con el mismo nombre."""