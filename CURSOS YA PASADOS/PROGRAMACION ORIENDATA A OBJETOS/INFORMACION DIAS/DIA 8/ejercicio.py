# # EJERCICIO = = = = = = = = = = = = = = = = = = = = = = = =

# class Empleado(): 
#     def __init__(self):
#         self.__salario = 300
        
#     @property 
#     def salario(self): 
#         return self.__salario
    
#     @salario.setter
#     def salario(self, salario_nuevo):
#         if salario_nuevo < 300: 
#             print ("ERROR. EL SALARIO DEBE DE SER MAYOR")
#         else: 
#             self.__salario = salario_nuevo
    
# usuario = Empleado()

# print(usuario.salario)
# usuario.salario = 500
# print(f"SALARIO MODIFICADO: ", usuario.salario)
            
# # EJERCICIO 2 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

# class Termostato_digital():
#     def __init__(self, temperatura_establecida):
#         self.__temperatura = temperatura_establecida 
        
#     @property
#     def temperatura(self): 
#         return self.__temperatura
    
#     @temperatura.setter
#     def temperatura(self, cambio_temperatura): 
#         while cambio_temperatura < 16 or cambio_temperatura > 24:
#             print("INVALIDO. LA TEMPERATURA DEBE SER ENTRE 16 Y 24 GRADOS.")
#             cambio_temperatura = float(input("INGRESE LA NUEVA TEMPERATURA:")) 
#         print("CAMBIANDO LA TEMPERATURA...")
#         self.__temperatura = cambio_temperatura
        
            
# entorno1 = Termostato_digital(20)
# print(entorno1.temperatura)
# print(f"TEMPERATURA MODIFICADA", entorno1.temperatura)

# # EJERCICIO 3 GUIADA = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

# class EmpleadoTienda(): 
#     #ATRIBUTOS DE CLASE
#     sueldo_minimo_legal = 300
#     cantidad_empleado = 0
    
#     #CONSTRUCTOR 
#     def __init__(self, nombre, id_empleado):
#         self.nombre = nombre
#         self.id = id_empleado
#         EmpleadoTienda.cantidad_empleado += 1 
#         #nombre
#         # id empleado
#         # cada vez que nace un empleado, modificamos el atributo de clase
        
#     # metodo de clase (la ley modifica el aumento del salario)
#     @classmethod
#     def aumento_nacional(cls, nuevo_salario):
#         cls.sueldo_minimo_legal = nuevo_salario
        
#         print("[COMUNICADO OFICIAL] EL GOBIERNO HA CAMBIADO EL SUELDO MINIMO")
#     # RECORDATORIO, usar cls y no self en los metodos de clase 
        
#     # mostrar recibos de pago 
#     def mostrar_recibos(self): 
#         print(f"EMPLEADO {self.id}: {self.nombre} | PAGO A RECIBIR: {EmpleadoTienda.sueldo_minimo_legal}")
#         # el objeto lee la info* compartida de su clase y datos propios 
        
# # PROGRAMA INICIAL 
# # print de encabezado 
# print("SISTEMA DE PLANILLA NACIONAL")

# # creamos 2 personas (empleados)
# trabajador1 = EmpleadoTienda("FER", 1)
# trabajador2 = EmpleadoTienda("JAVIER", 2)

# # comprobar que la variable compartida funciono(contador)
# print(f"TOTAL DE EMPLEADOS: {EmpleadoTienda.cantidad_empleado}")

# # dia de pago
# # generar los recibos de ambos empleados 
# trabajador1.mostrar_recibos()
# trabajador2.mostrar_recibos()


# # el gobierno interviene, aumentamos el sueldo minimo 
# EmpleadoTienda.aumento_nacional(400)

# # semana de pago, generar recibos de ambos empleados 
# trabajador1.mostrar_recibos()
# trabajador2.mostrar_recibos()

# # RETO INTEGRADOR = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

class CuentaBancaria(): 
    tasa_global = 0.05
    total_cuentas_creadas = 0
    
    def __init__(self, nombre_titular):
        self.__titular = nombre_titular
        self.__saldo = 0.0
        CuentaBancaria.total_cuentas_creadas += 1 
    
    @property
    def saldo(self): 
        return self.__saldo
    
    @property
    def titular(self): 
        return self.__titular
    
    @titular.setter
    def titular(self, nombre_titular): 
        if nombre_titular.strip() == "": 
            print("ERROR. EL NOMBRE NO PUEDE QUEDAR VACIO")
        else: 
            self.__titular = nombre_titular
            print(f"CAMBIO DE TITULAR: ANTIGUO {self.__titular} | NUEVO: {nombre_titular}")
    
    def depositar(self, cantidad): 
        if cantidad > 0:
            self.__saldo += cantidad
        else: 
            print("LA CANTIDAD DEBE DE SER MAYOR A 0")
            
    def retirar(self, cantidad): 
        if self.__saldo >= cantidad: 
            self.__saldo -= cantidad
            print("RETIRO EXITOSO.")
        else: 
            print("NO SE PUEDE REALIZAR EL RETIRO. PLATA INSUFICIENTE")
            
    def proyectar_interes(self): 
        ganancia_año = self.__saldo * CuentaBancaria.tasa_global
        print(f"GANANCIA A RECIBIR ESTE AÑO: {ganancia_año}")
        
    @classmethod
    def modificar_tasa_interes(cls, nuevo_tasa):
        cls.tasa_global = nuevo_tasa
        print("NUEVA TASA DE INTERES AGREGADA")
    
print("= = SISTEMA BANCARIO = =")
     
cuentauno = CuentaBancaria("Sofia")
cuentados = CuentaBancaria("fer")

print(f"\n TOTAL CUENTAS CREADAS: {CuentaBancaria.total_cuentas_creadas}")

cuentauno.depositar(10000)
cuentauno.retirar(5000)
cuentauno.proyectar_interes()

CuentaBancaria.modificar_tasa_interes(0.10)
cuentauno.proyectar_interes()

cuentauno.titular  = "  " 
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    