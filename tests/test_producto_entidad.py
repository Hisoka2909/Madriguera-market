"""Pruebas de las validaciones de la entidad Producto."""

import unittest

from entities.categoria import Categoria
from entities.excepciones import ErrorValidacion
from entities.producto import Producto


def _datos(**extra):
    datos = {
        "nombre": "Peluche de zorro",
        "descripcion": "Peluche mediano",
        "precio": 50000,
        "cantidad": 8,
        "categoria": Categoria.PELUCHES,
    }
    datos.update(extra)
    return datos


class PruebasProductoEntidad(unittest.TestCase):
    def test_producto_valido(self):
        self.assertEqual(Producto(**_datos()).categoria, Categoria.PELUCHES)

    def test_nombre_vacio_falla(self):
        with self.assertRaises(ErrorValidacion):
            Producto(**_datos(nombre="   "))

    def test_cantidad_negativa_falla(self):
        with self.assertRaises(ErrorValidacion):
            Producto(**_datos(cantidad=-1))

    def test_categoria_invalida_falla(self):
        with self.assertRaises(ErrorValidacion):
            Producto(**_datos(categoria="Armas"))

    def test_esta_por_agotarse(self):
        self.assertTrue(Producto(**_datos(cantidad=3)).esta_por_agotarse())
        self.assertFalse(Producto(**_datos(cantidad=30)).esta_por_agotarse())


if __name__ == "__main__":
    unittest.main()
