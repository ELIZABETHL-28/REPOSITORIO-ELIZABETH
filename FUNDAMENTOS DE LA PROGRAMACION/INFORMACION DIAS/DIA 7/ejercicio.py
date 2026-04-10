print ("--- GESTOR DE INVITADOS ---")
lista_invitados = []

def agregar_invitado(nombre):
    if nombre in lista_invitados:
        print("El invitado ya está en la lista")
    else:
        lista_invitados.append(nombre)
        print("Invitado agregado correctamente")

def mostrar_lista():
    if len(lista_invitados) == 0:
        print("La lista está vacía")
    else:
        print("LISTA DE INVITADOS")
        for invitado in lista_invitados:
            print("-", invitado)

def buscar_invitado(nombre):
    if nombre in lista_invitados:
        print("El invitado ya está en la lista")
    else:
        print("Nombre disponible")

def eliminar_invitado(nombre):
    if nombre in lista_invitados:
        lista_invitados.remove(nombre)
        print("Invitado eliminado")
    else:
        print("Ese invitado no está en la lista")  
        
def menu():
    print ("1. Registrar nuevo invitado")
    print ("2. Ver lista de invitado")
    print ("3. Buscar invitado")
    print ("4. Eliminar persona")
    print ("5. Salir ")
    
    opcion = input("Elige una opción: ")
    while True:

        match opcion:
            case "1":
                 nombre = input("Ingrese el nombre del invitado: ")
                 agregar_invitado(nombre) 
            case "2":
                print("- - - - - - - - -")
                mostrar_lista()
                print("- - - - - - - - -")

            case "3":
                nombre = input("Nombre a buscar: ")
                buscar_invitado(nombre)
            case "4":
                nombre = input("Nombre a eliminar: ")
                eliminar_invitado(nombre)
            case "5":    
                print("Saliendo del programa...")
                break
            case _:
                print("opcion invalida")

        opcion = input("Elige una opción: ")
menu()
