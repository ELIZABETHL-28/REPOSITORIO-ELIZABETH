# opcion = input ("seleccione (1-3)")

# if opcion == "1": 
#     print("registrando producto...")
# elif opcion == "2": 
#     print("mostrando inventario... ")
# elif opcion == "3": 
#     print("saliendo...")
# else: 
#     print(" opcion valida...")

print("BIENVENIDO AL SISTEMA DE INVETARIO")
print("1. registrar")
print("2. mostrar")
print("3. salir")

opcion = input ("selecione (1-3): ")
usuario = input("Ingrese su nombre de usuario: ")

match opcion:
    case ("registrar" | "1") if usuario == "admin":
        print("registrando producto...")
        nombre = input("Ingrese el nombre del producto: ")
        if nombre == "pantalon": 
             print("hahah")
        elif nombre == "camisa":
             print("hahah")
        else:
            print("hahah")
    case "2":
        print("mostrando inventario")
    case "3":
        print("saliendo...")
    case _:
        print("opcion valida")

## los cases deben de ir deacuerdo a lo que queremos 
## opcion = input ("selecione (1-3): ")
## match opcion: SI s