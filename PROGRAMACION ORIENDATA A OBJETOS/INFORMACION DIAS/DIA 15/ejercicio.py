# MODELO
class Libro(): 
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id 
        self.prestado = False 
        
# VISTA
class VistaLibro(): 
    def mostrar_menu(): 
        print("\n1 - AGREGAR NUEVO LIBRO\n2 - LISTA DE LIBROS \n 3 - PRESTAR LIBRO(POR ID) \n 4 - SALIR")
        return input("OPCION: ")
    
    @staticmethod
    def mostrar_lista(lista): 
        print("\nLISTA DE TAREAS: ")
        
        for libros in lista: 
    
        