"""Pruebas de las validaciones de la entidad Producto."""

import unittest

from entities.categoria import Categoria
from entities.excepciones import ErrorValidacion
from entities.producto import Usuario


def _datos(**extra):
    datos = {
        "nombre": "Lechi Hellhound",
        "email": "lechi@gmail.com",
        "documento": "616",
        "telefono": "666",
        "direccion": "Av 123",
    }
    datos.update(extra)
    return datos


class PruebaUsuarioEntidad(unittest.TestCase):
    def test_usuario_valido(self):
        self.assertEqual(Usuario(**_datos()))

    def test_nombre_vacio_falla(self):
        with self.assertRaises(ErrorValidacion):
            Usuario(**_datos(nombre=" "))

    def test_email_vacio_falla(self):
        with self.assertRaises(ErrorValidacion):
            Usuario(**_datos(email=" "))

    def test_documento_vacio_falla(self):
        with self.assertRaises(ErrorValidacion):
            Usuario(**_datos(documento=" "))

    def test_direccion_vacia_falla(self):
        with self.assertRaises(ErrorValidacion):
            Usuario(**_datos(direccion=" "))

    def test_nombre_vacio_falla(self):
        with self.assertRaises(ErrorValidacion):
            Usuario(**_datos(nombre=" "))
