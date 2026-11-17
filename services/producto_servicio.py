"""Logica de negocio del CRUD de Producto."""

from entities.excepciones import (
    ErrorValidacion,
    ProductoDuplicado,
    ProductoNoEncontrado,
)
from entities.producto import Producto

CAMPOS_EDITABLES = {
    "nombre",
    "descripcion",
    "precio",
    "cantidad",
    "categoria",
    "stock_minimo",
}


class ProductoServicio:
    def __init__(self, repositorio):
        self._repo = repositorio

    def crear(self, nombre, descripcion, precio, cantidad, categoria, stock_minimo=5):
        producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            cantidad=cantidad,
            categoria=categoria,
            stock_minimo=stock_minimo,
        )
        if self._repo.existe_nombre(producto.nombre):
            raise ProductoDuplicado(f"Ya existe un producto llamado '{producto.nombre}'.")
        return self._repo.crear(producto)

    def obtener(self, id_producto: int) -> Producto:
        producto = self._repo.obtener_por_id(id_producto)
        if producto is None:
            raise ProductoNoEncontrado(f"No existe el producto con id {id_producto}.")
        return producto

    def listar(self) -> list[Producto]:
        return self._repo.obtener_todos()

    def actualizar(self, id_producto: int, **cambios) -> Producto:
        actual = self.obtener(id_producto)

        invalidos = set(cambios) - CAMPOS_EDITABLES
        if invalidos:
            raise ErrorValidacion(f"Campos no editables: {', '.join(sorted(invalidos))}.")

        datos = {**actual.to_dict(), **cambios}
        actualizado = Producto.from_dict(datos)  # vuelve a validar todo

        if self._repo.existe_nombre(actualizado.nombre, excluir_id=id_producto):
            raise ProductoDuplicado(f"Ya existe un producto llamado '{actualizado.nombre}'.")
        return self._repo.actualizar(actualizado)

    def eliminar(self, id_producto: int) -> None:
        if not self._repo.eliminar(id_producto):
            raise ProductoNoEncontrado(f"No existe el producto con id {id_producto}.")

    def descontar_stock(self, id_producto: int, cantidad: int) -> Producto:
        """Resta unidades al inventario. Lo usara Pedido al confirmar una compra."""
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            raise ErrorValidacion("La cantidad a descontar debe ser un entero mayor que cero.")
        producto = self.obtener(id_producto)
        if cantidad > producto.cantidad:
            raise ErrorValidacion(
                f"Stock insuficiente: hay {producto.cantidad} y se piden {cantidad}."
            )
        return self.actualizar(id_producto, cantidad=producto.cantidad - cantidad)
