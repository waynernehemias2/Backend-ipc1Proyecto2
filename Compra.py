class Compra:
    def __init__(self,nombre,cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def getNombre(self):
        return self.nombre

    def getCantidad(self):
        return self.cantidad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setCantidad(self, cantidad):
        self.cantidad = cantidad