# class Mascota(): 
#     def alimentar(self):
#         if self.energia < 100: 
#             self.energia += 20
#             if self.energia > 100: 
#                 self.energia = 100
#             print(f"{self.nombre} ha comido. Estado de la bateria: {self.energia}")
#         else: 
#             print(f"{self.nombre} ya tiene energia completa")
            
#     def jugar(self): 
#         if self.energia >= 30: 
#             self.energia -= 30
#             print(f"HAS JUGADO CON {self.nombre}. ENERGIA ACTUAL")
            
            
            
# nombre = Mascota()
# energia = Mascota()
# =============================================================================================

# class Producto: 
#     def __init__(self):
#         pass

#     def funcional():
#         print()
    
# producto1 = Producto() #NUESTRO OBJETO
# producto1.precio = 500 # le agregamos un atributo a nuestro objeto manualmente

# producto2 = Producto() # 2DO objeto

# =============================================================================================

# class Libro (): 
#     #NUESTRO CONSTRUCCTOR EXIGE DOS INGREDIENTE EXTERNOS
#     def __init__(self, titulo_ingresado, autor_ingresado):
#         #GUARDAMOS LOS INGREDIENTES (ATRIBUTOS) EN EL INTERIOR DEL OBJETO
#         self.titulo = titulo_ingresado
#         self.autor = autor_ingresado

# # la fabricacion 
# # vamos a enviar los ingredientes a nuestra clase para crear un objeto 
# libro_nuevo = Libro("El principito", "Antoine de Saint-Exupery")
# libro_viejo = Libro("Don Quijote", "Miguel Cervantes")

# print(f"EL AUTOR REGISTRADO DEL LIBRO: {libro_nuevo.titulo} es {libro_nuevo.autor}")
# print(f"EL AUTOR REGISTRADO DEL LIBRO: {libro_viejo.titulo} es {libro_viejo.autor}")
# =============================================================================================

# class Alcancia: 
#     def __init__(self):
#         self.dinero_guardado = 0
#         #el atributo es lo que le pertenece directamente a la clase
        
#         # un parametro es el valor que le da dentro del parentesis 
#     def depositar_dinero(self, cantidad): 
#         # sumar el parametro al atributo 
#         # self.dinero_guardado = self.dinero_guardado + cantidad ES LO MISMO A LA DE ABAJO
#         self.dinero_guardado += cantidad
        
#     def mostrar_ahorros(self): 
#         print(f"EL DINERO AHORRADO ES: {self.dinero_guardado}")
        
#   # crear un objeto 
# mi_chanchito = Alcancia()
# # acciones 
# mi_chanchito.depositar_dinero(500)
# mi_chanchito.depositar_dinero(1200)

# mi_chanchito.mostrar_ahorros()


# alcancia1 = Alcancia()
# alcancia1.depositar_dinero(5000)
# alcancia1.mostrar_ahorros()

# =============================================================================================

class Televisor: 
    def __init__(self, marca):
        self.marca = marca
        self.encendido = False # SERA UN ESTADO INICIAL DE APAGADO 
        self.volumen = 10 # ESTADO INICIAL: VOLUMEN 10
        
    def presionar_boton_encendido(self): 
        # si estaba apagado (false), lo prendemos (true)
        if not self.encendido: #ES LO MISMO DE ABAJO LOS DOS DAN TRUE
        # if self.encendido == False: 
            self.encendido = True
            print(F"El televisor {self.marca} se ha encendido")
        # si estaba encendido (true), lo apagamos (false)
        else: 
            self.encendido = False 
            
    def subir_volumen(self): 
        # if self.encendido == True: LOS DOS DAN TRUE, ES LO MISMO
        if  self.encendido: 
            self.volumen += 1 
            print(f"El volumen actural: {self.volumen}")
        else: 
            print("ERROR: no se puede subir el volumen. El televisor esta apagado...")
        
tv1 = Televisor("SAMSUNG")

tv1.subir_volumen()    
tv1.presionar_boton_encendido()

tv1.subir_volumen()    
tv1.subir_volumen()    

tv1.presionar_boton_encendido()        
tv1.presionar_boton_encendido()        

        














