# paso 1, definir la clase 
# tenemos que usar la palabra reservada, `class` 
# al final del nombre de la clase, se debe de colocar ":"

class ClienteFrecuente: 
    pass 

# paso 2: la instanciacion: ES UNA ACCION, crea un objeto a partir de la clase, se crea una instanciacion 
cliente1 = ClienteFrecuente()

cliente2 = ClienteFrecuente()

print(ClienteFrecuente)
print(cliente1)
print(cliente2)

# comprobando el plano(clase)
print(type(cliente1))

# comprobando que son objetos diferentes, nos da un identificar unico, 
print(id(cliente1))
print(id(cliente1))

# # paso 3, creamos una variable y una funcion 
# nombre_cliente = "Juan Perez"

# def registrar_cliente(): 
#     print("El cliente ha sido guardado")

# ---------------------------------------------------------------------------------

# EJERCICIO 1 
class Cajero: 
    pass 

class Inventario: 
    pass 

class VehiculoReparto: 
    pass 

cajero1 = Cajero()
cajero2 = Cajero()

print("CAJEROS: ")
print(cajero1)
print(cajero2)


inventario_principal = Inventario()
print(inventario_principal)

vehiculo1 = VehiculoReparto()
vehiculo2 = VehiculoReparto()
vehiculo3 = VehiculoReparto()

print(vehiculo1)
print(vehiculo2)
print(vehiculo3)
# ---------------------------------------------------------------------------------

# EJERCICIO 2
class FacturaEmitida:
    pass 

class TerminalDePago: 
    pass

factura_001 = FacturaEmitida()
factura_002 = FacturaEmitida()

terminal_principal = TerminalDePago()

print(type(terminal_principal))

print(id(factura_001))
print(id(factura_002))


if (id(factura_001)) == (id(factura_002)):
    print("EL ID ES IGUAL")  
else: 
    print("EL ID NO ES IGUAL")