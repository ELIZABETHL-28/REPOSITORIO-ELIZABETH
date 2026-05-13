# class Bateria():
#     def __init__(self):
#         self.porcentaje = 100
        
#     def descargar(self): 
#         self.porcentaje -= 10
#         print("BATERIA AL PORCENTAJE", {self.porcentaje})
        
# class Celular(): 
#     def __init__(self, marca):
#         self.marca = marca 
#         self.energia = Bateria()
        
#     def usar_app(self): 
#         print("ABRIENDO APLICACION...")
#         self.energia.descargar()
        
# mi_phone = Bateria("SAMSUNG")
# mi_phone.energia.descargar()
# mi_phone.energia.descargar()

# #VER IMAGEN DEL EJERCICIO DE LA CHICA 

# ======================================================================


# class Arma(): 
#     def __init__(self, nombre, puntos_dano):
#         self.nombre = nombre
#         self.puntos_dano = puntos_dano
        
# class Guerrero():
#     def __init__(self, nombre, arma_equipada):
#         self.nombre = nombre
#         self.arma = arma_equipada
        
#     def atacar(self): 
#         print({self.nombre}, "ATACA CON", {self.arma}, "CAUSANDO", {self.puntos_dano}, "DE DAÑO!")
        
        
# usuario1 = Arma("ESPADA LARGA", 50)
# golpe1 = Guerrero("KIRA", usuario1)
# golpe1.atacar()

# REBICAR PORQUE ME CAUSA UN ERROR, TENGO ALGO MAL0 !!!!!!!
            
# ======================================================================

class Libro(): 
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor 
        
    def __str__(self):
        return f'--{self.titulo}-- ESCRITO POR --{self.autor}--'        
    
class Bibliotecas(): 
    def __init__(self, nombre_sucursal):
        self.nombre_sucursal = nombre_sucursal
        self.catalogo = []
        
    def agregar_libro(self, nuevo_libro): 
        self.catalogo.append(nuevo_libro)

    def mostrar_inventario(self): 
        print("INVENTARIO DE: ", self.nombre_sucursal)
        for libro in self.catalogo: 
            print(libro)
            
libro1 = Libro("1984", "George Orwell")
libro2 = Libro("Guerra y Paz", "Lev Tolstói")
libro3 = Libro("En busca del tiempo perdido", "Marcel Proust")
biblioteca_original = Bibliotecas("BIBLIOTECA GENERAL") 
biblioteca_original.agregar_libro(libro1)
biblioteca_original.agregar_libro(libro2)
biblioteca_original.agregar_libro(libro3)

biblioteca_original.mostrar_inventario()  
