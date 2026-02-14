from excepciones import ClienteNoEncontradoError
from servicios.logger import registrar


class GestorClientes:

    def __init__(self):
        # encapsulado (buena práctica POO)
        self._clientes = []

    # CREATE
    def agregar(self, cliente):
        if cliente in self._clientes:
            raise ValueError("El cliente ya existe")

        self._clientes.append(cliente)
        registrar(f"Cliente agregado: {cliente}")

    # READ
    def listar(self):
        return list(self._clientes)  # copia segura

    def buscar(self, email):
        for c in self._clientes:
            if c.email == email:
                return c

        raise ClienteNoEncontradoError("Cliente no encontrado")

    # UPDATE
    def actualizar(self, email, **datos):
        cliente = self.buscar(email)

        for clave, valor in datos.items():
            setattr(cliente, clave, valor)

        registrar(f"Cliente actualizado: {cliente}")

    # DELETE
    def eliminar(self, email):
        cliente = self.buscar(email)
        self._clientes.remove(cliente)
        registrar(f"Cliente eliminado: {cliente}")