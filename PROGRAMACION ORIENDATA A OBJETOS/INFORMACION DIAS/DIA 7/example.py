# class Cuenta():
#     def __init__(self, saldo_inicial):
#         self.nombre = "PUBLICA"
#         self.__saldo = saldo_inicial #LOS DOS GUIONES BAJOS ME INDICA QUE ESO ES PRIVADO
        
# mi_cuenta = Cuenta(1000)
# print(mi_cuenta.nombre)
# print(mi_cuenta.__saldo) # ERROR  python no permite acceder a atributos privados desde fuera de la clase

# # -----------------------------------------------------------------------------------------------------------------


class UsuarioBancario():
    def __init__(self, nombre_ingresado, pin_ingresado):
        self.nombre = nombre_ingresado
        #atributo privado
        self.__pin = pin_ingresado
        
    # get tradicional (ventanilla para consultar)
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, nuevo_pin):
        #validacion 
        if len(str(nuevo_pin)) == 4:
            self.__pin = nuevo_pin
            print("OPERACION EXITOSA. PIN ACTUALIZADO")
        else: 
            print("ERROR: el pin debe de tener exactamente 4 digitos")
   
print("==SISTEMA DE SEGURIDAD==")
cliente = UsuarioBancario("Diego", 1234)         

# primer intento de hackeo: intentar accdeder directamente al atributo privado

print(cliente.get_pin())
pin_cliente = cliente.get_pin()
print(pin_cliente)

cliente.set_pin(5844) #operacoin exitosa


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            