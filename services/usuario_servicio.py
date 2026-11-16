"""Logica de negocio del CRUD de Usuario."""

from entities.excepciones import (
    ErrorValidacion,
    UsuarioDuplicado,
    UsuarioNoEncontrado,
)
from entities.usuario import Usuario

CAMPOS_EDITABLES = {
    "nombre",
    "email",
    "telefono",
    "direccion",
    "estado",
}


class UsuarioServicio:

    def __init__(self, repositorio):
        self._repo = repositorio

    def crear(self, nombre, email, documento, telefono, direccion, estado="Activo"):
        usuario = Usuario(
            nombre=nombre,
            email=email,
            documento=documento,
            telefono=telefono,
            direccion=direccion,
            estado=estado,
        )
        if self._repo.existe_email():
            raise UsuarioDuplicado(
                f"Ya existe un usuario con el correo '{usuario.email}' UnU"
            )
        if self._repo.existe_documento():
            raise UsuarioDuplicado(
                f"Ya existe un usuario con el documento '{usuario.documento}' OnO"
            )
        return self._repo.crear(usuario)

    def obtener(self, id: int) -> Usuario:
        usuario = self._repo.obtener_por_id(id)
        if usuario is None:
            raise UsuarioNoEncontrado(f"No existe el usuario con id {id} OnO")
        return usuario

    def listar(self) -> list[Usuario]:
        return self._repo.obtener_todos()

    def editar_datos(self, id: int, **cambios) -> Usuario:
        actual = self.obtener(id)

        invalidos = set(cambios) - CAMPOS_EDITABLES
        if invalidos:
            raise ErrorValidacion(
                f"Campos no editables TwT: {', '.join(sorted(invalidos))}"
            )

        datos = {**actual.to_dict(), **cambios}
        actualizado = Usuario.from_dict(datos)

        if self._repo.existe_email(actualizado.email, excluir_id=id):
            raise UsuarioDuplicado(
                f"Ya existe un usuario con ese email OnO: '{actualizado.email}'"
            )
        if self._repo.existe_documento(actualizado.documento, excluir_id=id):
            raise UsuarioDuplicado(
                f"Ya existe un usuario con ese documento OnO: '{actualizado.documento}'"
            )
        return self._repo.actualizar(actualizado)

    def eliminar(self, id: int) -> None:
        if not self._repo.eliminar(id):
            raise UsuarioNoEncontrado(f"No existe un usuario con el ID {id} UnU")
