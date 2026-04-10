# class LibroFisico():
    
#     def __init__(self, titulo, autor, precio=100):
#         self.titulo = titulo
#         self.autor = autor
#         self.precio = precio
#         self.disponible = True 
        
#     def prestar_libro(self):
#         if self.disponible == False: 
#             print(" EL LIBRO NO ESTA DISPONIBLE")
#         else: 
#             print(f"LIBRO {self.titulo} DISPONIBLE! LIBRO PRESTADO Y SU PRECIO ES {self.precio}")
#             self.disponible = False
    
#     def cambiar_nombre(self, nuevo_nombre):
#         self.titulo = nuevo_nombre
#         print(f"EL NUEVO NOMBRE DEL LIBRO ES: {self.titulo}")
         
# libro1 = LibroFisico("EL QUIJOTE", "MIGUEL DE CERVANTES", 200)
# libro2 = LibroFisico("CIEN AÑOS DE SOLEDAD", "GABRIEL CARCIA MARQUEZ")

# libro1.prestar_libro()
# libro1.prestar_libro()    

# libro2.prestar_libro()    
# libro1.cambiar_nombre("EL QUIJOTE DE LA MANCHA")



class AireAcondicionado(): 
    def __init__(self):
        self.temperatura = 24 
        
    def bajar_temperatura(self, grados): 
        self.temperatura = grados
        if self.temperatura < 16: 
            print("TEMPERATURA MENOS DE 16 GRADOS. DENEGADA ")
        else: 
            self.temperatura -= grados
            print(f"TEMPERATURA EN AMBIENTE: {self.temperatura}")
            
          
usuario1 = AireAcondicionado()    

usuario1.bajar_temperatura(10)