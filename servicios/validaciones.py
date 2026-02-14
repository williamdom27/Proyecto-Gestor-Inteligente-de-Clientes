import re
from excepciones import ValidacionError


def validar_email(email):
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(patron, email):
        raise ValidacionError("Email inválido")


def validar_telefono(telefono):
    if not telefono.isdigit() or len(telefono) < 8:
        raise ValidacionError("Teléfono inválido")


def validar_texto(valor, campo):
    if not valor.strip():
        raise ValidacionError(f"{campo} no puede estar vacío")