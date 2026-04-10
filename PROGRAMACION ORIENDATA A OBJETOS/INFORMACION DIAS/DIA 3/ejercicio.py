# class Cajero(): 
#     def __init__(self, nombre_cajero, id_cajero):
#         self.nombre = nombre_cajero
#         self.id = id_cajero
#         self.dinero_en_caja = 0
        
#     def cobrar_articulo(self, precio_del_articulo): 
#         self.dinero_en_caja += precio_del_articulo
        
#     def mostrar_dinero_caja(self): 
#         print(f"CAJERO: {self.nombre} ID: {self.id}")
#         print(f"PLATA EXISTENTE EN CAJA: {self.dinero_en_caja}")
        
        
        
# cajero1 = Cajero("Mauricio", 123)
# cajero2 = Cajero("Rebeca", 456)

# cajero1.cobrar_articulo(200)
# cajero1.cobrar_articulo(500)
# cajero1.mostrar_dinero_caja()

# cajero2.cobrar_articulo(600)
# cajero2.mostrar_dinero_caja()

# # =============================================================================

# class Televisor: 
#     def __init__(self, marca):
#         self.marca = marca
#         self.encendido = False # SERA UN ESTADO INICIAL DE APAGADO 
#         self.volumen = 10 # ESTADO INICIAL: VOLUMEN 10
        
#     def presionar_boton_encendido(self): 
#         # si estaba apagado (false), lo prendemos (true)
#         if not self.encendido: #ES LO MISMO DE ABAJO LOS DOS DAN TRUE
#         # if self.encendido == False: 
#             self.encendido = True
#             print(F"El televisor {self.marca} se ha encendido")
#         # si estaba encendido (true), lo apagamos (false)
#         else: 
#             self.encendido = False 
            
#     def subir_volumen(self): 
#         # if self.encendido == True: LOS DOS DAN TRUE, ES LO MISMO
#         if  self.encendido: 
#             self.volumen += 1 
#             print(f"El volumen actural: {self.volumen}")
#         else: 
#             print("ERROR: no se puede subir el volumen. El televisor esta apagado...")
        
# tv1 = Televisor("SAMSUNG")

# tv1.subir_volumen()    
# tv1.presionar_boton_encendido()

# tv1.subir_volumen()    
# tv1.subir_volumen()    

# tv1.presionar_boton_encendido()        
# tv1.presionar_boton_encendido()        

# # =============================================================================

# RETO 
class Personaje():
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.puntos_de_vida = 100
        self.esta_vivo = True

    def recibir_dano(self, cantidad_dano):
        self.puntos_de_vida -= cantidad_dano

        if self.puntos_de_vida <= 0:
            self.esta_vivo = False
            print(f"{self.nombre} ha sido derrotado.")
        else:
            print(f"{self.nombre} recibió daño. Vida restante: {self.puntos_de_vida}")

personaje_1 = Personaje("CAPITAN AMERICA")
personaje_2 = Personaje("ROBIN")

personaje_1.recibir_dano(20)
personaje_1.recibir_dano(30) 
print ("=======================================================")  

personaje_2.recibir_dano(80)
personaje_2.recibir_dano(20)
print ("=======================================================")  
                                                                                                              

if personaje_1.esta_vivo:
    print(f"{personaje_1.nombre} sigue con vida.")
else:
    print(f"{personaje_1.nombre} está muerto.")
  
print ("=======================================================")  
    
if personaje_2.esta_vivo:
    print(f"{personaje_2.nombre} sigue con vida.")
else:
    print(f"{personaje_2.nombre} está muerto.")