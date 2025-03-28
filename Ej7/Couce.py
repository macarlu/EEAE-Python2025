class Producto:

    def __init__ (self,nombre,precio,cantidad):

        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_inventario (self):

        self.inventario= self.precio * self.cantidad

        return (f"El valor total del inventario de {self.nombre} es:{self.inventario}")

producto1 = Producto("pilas",20,100)
producto2 = Producto("Martillos",75,350)


print(producto1.valor_inventario())
print(producto2.valor_inventario())
