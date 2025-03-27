'''Crea una clase Producto con atributos para nombre, precio y cantidad en stock.
Añade un método que calcule el valor total del inventario (precio × cantidad).'''
class Producto:
    def __init__(self, name, price, stock):
        self.nombre = name
        self.precio = price
        self.cantidad = stock
    def total_value (self):
        self.inventario = self.precio * self.cantidad
        return self.inventario
Producto1 = Producto ("jamón",75,2)
print ("El total del inventario es de ", Producto1.total_value())
