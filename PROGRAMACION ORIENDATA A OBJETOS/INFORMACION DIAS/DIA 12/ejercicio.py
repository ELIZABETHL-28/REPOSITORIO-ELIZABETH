# import random

# class SableDeLuz(): 
#     def __init__(self):
#         self.energia = 100
        
#     def recargar(self): 
#         if self.energia < 100: 
#             self.energia += 10
#             if self.energia > 100: 
#                 self.energia = 100
    
#     def __sub__(self, cantidad):
#         self.energia -= cantidad
#         if self.energia < 0:
#             self.energia -= 10
#         return self
    
# def log(sable): # LOG ES PARA MOSTRAR CUANTO ES EL ESTADO. 
#     print(f"ENERGIA ACITAL DEL SABLE: {sable.energia}")
    
# sable = SableDeLuz()

# ataque = random.randint(10, 40)
# sable - ataque 

# sable.recargar()
# log(sable)

# ========================================================================================
# from abc import ABC, abstractmethod

# class Trabajador(ABC): 
#     def __init__(self, persona):
#         self.persona = persona
        
#     @abstractmethod
#     def realizar_tarea(self):
#         pass   
    
# class Ingeniero(Trabajador): 
#     def realizar_tarea(self):
#         print("DISEÑANDO PLANOS")
        
# class Ingeniero(Trabajador): 
#     def realizar_tarea(self):
#         pass 
        
# try: 
#     doc_invalido = Trabajador ("Persona trabajando")
# except: 
#     print("-BLOQUEO DE SEGURIDAD-")
    
    
# inge = Ingeniero("REPORTE DE VENTAS")
# inge.realizar_tarea()

# medic = Ingeniero("ESTERNOCLEIDOMASTOIDEO")
# medic.realizar_tarea()

#========================================================================================

# from abc import ABC, abstractmethod

# class VehiculoTerrestre(ABC): 
#     @abstractmethod
#     def conducir_ruedas(self): 
#         pass
    
# class VehiculoAcuatico(ABC): 
#     @abstractmethod
#     def encender_helices(self): 
#         pass 
    
# class VehiculoAnfibio(VehiculoTerrestre, VehiculoAcuatico): 
#     def conducir_ruedas(self):
#         print("ACTIVANDO TRACCION 4X4 EN TERRENO ROCOSO")
        
#     def encender_helices(self):
#         print("RETRAYENDO RUEDAS Y ACTIVANDO PROPULSION ACUATICA")
    
# class AutoComun(VehiculoTerrestre): 
#     def conducir_ruedas(self):
#         print("AHORA VA CAMINANDO...") 
    
# class Lancha(VehiculoAcuatico): 
#     def encender_helices(self):
#         print("LA LANCHA ANDA RECORRIENDO") 
    
# primer_auto = AutoComun()
# primer_lancha = Lancha()
# primer_anfibio = VehiculoAnfibio()

# terrestre = [primer_auto, primer_anfibio]

# for carros in terrestre: 
#     carros.conducir_ruedas()
    
# acuaticos = [primer_lancha, primer_anfibio]

# for elemento in acuaticos: 
#     elemento.encender_helices()
    




