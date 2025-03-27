'''Crea una clase CuentaBancaria con atributos para titular y saldo.
Añade métodos para depositar, retirar y consultar el saldo. 
Usa el manejo de excepciones para evitar saldos negativos.'''
class CuentaBancaria:
    def __init__(self, owner, cash):
        self.titular = owner
        self.saldo = cash
        if self.saldo<0:
            raise ValueError("El saldo debe de ser positivo")
    def ingresar (self, income):
        self.verde = income + self.saldo
        return self.verde
    def retirar (self, outcome):
        self.rojo = self.saldo - outcome
        return self.rojo
    def consulta_saldo (self):
        return self.saldo
try:
    cuentasuina= CuentaBancaria ("Couce", -1000)
    print (cuentasuina.consulta_saldo())
except ValueError as e:
    print (f"Error: {e}")
#cuentasuina = CuentaBancaria ("Canosa", 22500)
#print (cuentasuina.ingresar(2000))
#print (cuentasuina.retirar(1000))
#print (cuentasuina.consulta_saldo())
    
