# # EJEMPLO 1 
# from abc import ABC, abstractmethod
# class Personaje(ABC):
#     @abstractmethod
#     def atacar(self): 
#         pass
    
# class Guerrero(Personaje): 
#     def atacar(self): return "Ataca con espada"
    
# class Mago(Personaje): 
#     def atacar(self): return "Ataca con magia"
    
# # LA FABRICA (EL CORAZON DEL PATRON)
# class FabricaPersonajes(): 
#     @staticmethod # VIVE DENTRO DE LA CLASE, NO SABE NADA DE LA CLASE. SOLO NOR SIRVE PARA 
#     # UNA FUNCION NORMAL COMUN, POR ORGANIZACION ENTONCES NO VAMOS A METER EL SELF.
#     def crear_personaje(tipo): 
#         #ESTE METODO CENTRALIZA TODA LA LOGICA DE CRECION 
#         tipo = tipo.lower()
        
#         if tipo == "guerrero":
#             return Guerrero()
#         elif tipo == "mago": 
#             return Mago()
#         else: 
#             raise ValueError(f"LA FABRICA NO SABE CREAR: {tipo}")
        
# try: 
#     eleccion = input("QUE PERSONAJE DESEA: GUERREO/MAGO)")
#     heroe = FabricaPersonajes.crear_personaje(eleccion)
#     print("heroe.atacar")
    
# except ValueError as error:
#      print (error)
        
        
# fabrica = FabricaPersonajes()
# fabrica.crear_personaje()

# personaje = FabricaPersonajes.crear_personaje("mago")
# # por organizacion

# =================================================================================
# EJEMPLO 2 MODELO (LOGICA PURA)

class Tarea(): 
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False 

# VISTA        
class VistaTarea(): 
    @staticmethod
    def mostrar_menu():
        print("\n1 - AGREGAR TAREA\n2 - MOSTRAR TAREA \n SALIR")
        return input("OPCION: ")
    
    @staticmethod
    def mostrar_lista(lista): 
        print("\nLISTA DE TAREAS: ")
        
        for tarea in lista:
            estado = "Completada" if tarea.completa else "Pendiente" 
            print(f"{tarea.descripcion} esta en estado: {tarea.completada}" )
      
    @staticmethod
    def solicitar_descripcion(): 
        return input("DESCRIPCION DE LA TEREA: ")  
    
    @staticmethod
    def mostrar_mensaje(mensaje): 
        print(mensaje)
# CONTROLADOR 
class ControladorTareas(): 
    def __init__(self):
        self.tareas = []
        self.vista = VistaTarea()
        
    def ejecutar(self): 
        while True: 
            opcion = self.vista.mostrar_menu()
            if opcion == "1": 
                descripcion = self.vista.solicitar_descripcion()
                tarea = Tarea(descripcion)
                self.tareas.append(tarea)
            elif opcion == "2": 
                self.vista.mostrar_lista(self.tareas)
            elif opcion == "3": 
                self.vista.mostrar_mensaje("SALIENDO...")
                
if __name__ == "__main__": 
    controlador = ControladorTareas()
    controlador = controlador.ejecutar()
    
                
                
                
                
        
            
        