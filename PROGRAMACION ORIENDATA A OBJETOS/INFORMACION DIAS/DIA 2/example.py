# # Esto sera nuestro molde para la clase producto 
# class Producto(): 
#     pass 

# # fabricar dos obejtos fisicos e independientes 
# articulo_1 = Producto()
# articulo_2 = Producto()

# # le vamos a asignar atributos (CARACTERISTICAS) a cada uno 
# # sintaxis: objeto.atributo = valor
# articulo_1.nombre = "Camiseta"
# articulo_1.precio = 19.99
# articulo_1.cantidad = 10

# articulo_2.nombre = "Pantalon"
# articulo_2.precio = 39.99
# articulo_2.cantidad = 5

# print(f"Articulo 1:  {articulo_1.nombre}, Precio: {articulo_1.precio}, Cantidad: {articulo_1.cantidad}")
# print(f"Articulo 2:  {articulo_2.nombre}, Precio: {articulo_2.precio}, Cantidad: {articulo_2.cantidad}")

# # ---------------------------------------------------------------------------------------------------------------------------------------------

# class Empleado(): 
#     pass 

# empleado_1 = Empleado()
# empleado_2 = Empleado()
# empleado_3 = Empleado()

# empleado_1.nombre = "Andrew"
# empleado_1.cargo = "Gerente"
# empleado_1.salario = 9000

# empleado_2.nombre = "David"
# empleado_2.cargo = "Cajero"
# empleado_2.salario = 5000

# empleado_3.nombre = "Hector"
# empleado_3.cargo = "Bodeguero"
# empleado_3.salario = 5000


# print(f"EMPLEADO 1:  {empleado_1.nombre}, CARGO: {empleado_1.cargo}, SALARIO: {empleado_1.salario}")
# print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
# print(f"EMPLEADO 2:  {empleado_2.nombre}, CARGO: {empleado_2.cargo}, SALARIO: {empleado_2.salario}")
# print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
# print(f"EMPLEADO 3:  {empleado_3.nombre}, CARGO: {empleado_3.cargo}, SALARIO: {empleado_3.salario}")
# print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


# # ---------------------------------------------------------------------------------------------------------------------------------------------
# class Empleado():
#     def saludar_cliente(self): 
#         print(f"HOLA, me llamo {self.nombre}, bienvenido a nuestra tienda")

# #fabricamos el objeto 
# cajero = Empleado()
# bodeguero = Empleado()

# cajero.nombre = "Diego"
# bodeguero.nombre = "Luis"

# cajero.saludar_cliente()
# bodeguero.saludar_cliente()

# #---------------------------------------------------------------------------------------------------------------------------------------------

# class CajaRegistradora():

#     def mostrar_dinero_actual(self): 
#         print(f"/DINERO ACTUAL: {self.dinero}")

#     def procesar_venta(self):
#         self.dinero += 500
#         print(f"VENTA PROCESADA (+500): ")


# caja = CajaRegistradora()
# caja.dinero = 2000

# caja.mostrar_dinero_actual()
# caja.procesar_venta()
# caja.mostrar_dinero_actual()

# #---------------------------------------------------------------------------------------------------------------------------------------------

class TarjetaVIP(): 

    def mostrar_puntos(self): 
        print(f"SUS PUNTOS ACUMULADOS SON: {self.puntos}")
    
    def sumar_puntos(self):
        self.puntos += 50
        print("SE HAN SUMADO 50 puntos por su compra")


tarjeta_carlos = TarjetaVIP()
tarjeta_carlos.puntos = 100 

tarjeta_carlos.mostrar_puntos()
tarjeta_carlos.sumar_puntos()
tarjeta_carlos.mostrar_puntos()






