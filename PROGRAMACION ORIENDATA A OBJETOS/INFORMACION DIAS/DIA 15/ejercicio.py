# MODELO
class Libro(): 
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.prestado = False 

# VISTA
class VistaBiblioteca(): 
    @staticmethod   
    def mostrar_menu(): 
        print("\n1 - AGREGAR NUEVO LIBRO\n2 - LISTA DE LIBROS \n 3 - PRESTAR LIBRO(POR ID) \n 4 - SALIR")
        return input("OPCION: ")
    
    @staticmethod
    def pedir_datos_libro():
        print("============================================")
        id = input("ID DEL LIBRO: ")
        titulo = input("TITULO: ")
        autor = input("AUTOR: ")
        print("============================================")
        return id, titulo, autor 
    
    @staticmethod
    def buscar_por_id(): 
        return input("ID-LIBRO A PRESTAR: ")
    
    @staticmethod
    def mostrar_lista(lista): 
        print("============================================")
        print("\nLISTA DE LIBROS: ")
        
        for libros in lista: 
            estado = "Prestado" if libros.prestado else "Disponible"
            print(f"{libros.id} - {libros.titulo} - {libros.autor} - {estado}") 
        print("============================================")   

    
    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)

# CONTROLADOR 
class ControladorBiblioteca():
    def __init__(self):
        self.libros = []
        self.vista = VistaBiblioteca()

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()

            if opcion == "1":
                id, titulo, autor = self.vista.pedir_datos_libro()
                libro = Libro(id, titulo, autor)
                self.libros.append(libro)

            elif opcion == "2":
                self.vista.mostrar_lista(self.libros)

            elif opcion == "3":
                id = self.vista.buscar_por_id()
                encontrado = False
                for libro in self.libros:
                    if libro.id == id and not libro.prestado:
                        libro.prestado = True
                        encontrado = True
                        break

                if encontrado:
                    self.vista.mostrar_mensaje("LIBRO PRESTADO.")
                else:
                    self.vista.mostrar_mensaje("LIBRO NO ENCONTRADO/YA PRESTADO.")

            elif opcion == "4":
                self.vista.mostrar_mensaje("SALIENDO...")
                break

if __name__ == "__main__":
    controlador = ControladorBiblioteca()
    controlador.ejecutar()
