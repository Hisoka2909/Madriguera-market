"""Excepciones compartidas por todo el proyecto"""


class ErrorValidacion(ValueError):
    """Se lanza cuando los datos de una entidad no son validos"""


class ProductoNoEncontrado(LookupError):
    """Se lanza cuando se busca un producto que no existe."""


class ProductoDuplicado(ValueError):
    """Se lanza cuando ya existe un producto con el mismo nombre."""


class UsuarioDuplicado(ValueError):
    """Se lanza cuando ya existe un usuario con el mismo correo electrónico o documento. 7-7"""


class UsuarioNoEncontrado(LookupError):
    """Se lanza cuando se busca un usuario que no existe. O,w,O"""


class PedidoNoEncontrado(LookupError):
    """Se lanza cuando se busca un pedido que no existe. UvU"""
