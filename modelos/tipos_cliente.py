from modelos.cliente import Cliente


class ClienteRegular(Cliente):
    def tipo(self):
        return "Regular"


class ClientePremium(Cliente):
    def tipo(self):
        return "Premium"

    def descuento(self):
        return 0.10


class ClienteCorporativo(Cliente):
    def tipo(self):
        return "Corporativo"

    def descuento(self):
        return 0.20