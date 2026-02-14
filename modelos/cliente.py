from servicios.validaciones import *
from excepciones import ValidacionError


class Cliente:
    def __init__(self, nombre, email, telefono, direccion):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

    # Encapsulación con propiedades
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        validar_email(valor)
        self._email = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        validar_telefono(valor)
        self._telefono = valor

    def tipo(self):
        return "Base"

    def descuento(self):
        return 0

    def __str__(self):
        return f"{self.nombre} ({self.tipo()})"

    def __eq__(self, other):
        return self.email == other.email