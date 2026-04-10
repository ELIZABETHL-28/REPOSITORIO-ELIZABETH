# class Temperatura: 
#     def __init__(self):
#         self.__grados = 20
        
#     @property
#     def grados(self): 
#         return self.__grados
    
#     @grados.setter
#     def grados(self, nuevo_grado):
#         if nuevo_grado < 0: 
#             print("TEMPERATURA INVALIDA")
#         else: 
#             self.__grados = nuevo_grado 
    
# clima = Temperatura()
# # CON EL METODO TRADICIONAL. NECESITAMOS USAR EL clima.get_grados() para obtener el valor de grados 
# # clima.__grados NO FUNCIONA 

# print(clima.grados)
# clima.grados = 50
# print(clima.grados)

# # EJEMPLO ATRIBUTOS Y METODOS DE CLASE  2 = = = = = = = = = = = = = = = = = = = = = = = =

# class Tienda(): 

#     impuesto_iva = 0.13
    
#     def __init__(self, productos):
#         self.productos = productos
        
#     @classmethod
#     def cambiar_impuesto(cls, nuevo_impuesto):
#         cls.impuesto_iva = nuevo_impuesto
        
# Tienda.cambiar_impuesto(0.15)      

  
# print(Tienda.impuesto_iva) # 0.13

# # = = = = = = = = = = = = = = = = = = = = = = = =
class RegistroVisitantes():
    total_personas = 0
    
    def __init__(self, nombre_visitante):
        self.nombre = nombre_visitante
        
        # self.total_personas = 1 ERROR COMUN 
        RegistroVisitantes.total_personas += 1 
        print(f"[{self.nombre} ha ingresado]. La pizarra global ahora marca: {RegistroVisitantes.total_personas}")
# NACE EL PRIMER OBJETO Y SUBE A 1 
persona1 = RegistroVisitantes("Fer")
# NACE EL SEGUNDO OBJETO Y SUBE A 2
persona2 = RegistroVisitantes("Javier")
# NACE EL TERCER OBJETO Y SUBE A 3 
persona3 = RegistroVisitantes("Helen")

print(f"\n TOTAL FINAL DEL DIA DE PERSONAS ES: {RegistroVisitantes.total_personas}")
    
 
