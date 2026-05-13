# aca le enseño que saludar se hace esto... 
def saludo(nombre): 
    print("HOLAAAAAA!")
    print(f"COMO ESTAS?, {nombre}")

def despedida(nombre): 
    print("Adios, que tengas un excelente dia")
    print(f"Hasta luego! {nombre}")

def calculo_impuestos (precio):
   impuesto = precio * 0.15
   total = precio + impuesto
  
   return total

def realizar_operacion (a, b): 
    return a + b  


# funcion con vario puntos de retorno
def generar_mensaje(nombre):
    if nombre == "Alice":
        return "Hola Alice, ¿cómo estás?"
    
        # esto no se va a ejecutar porque el return anterior ya terminó la función
        apellido = input("Ingrese su apellido: ")
        return f"Hola {nombre} {apellido}, ¿cómo estás?"
    
    elif nombre == "Bob":
        return "Hola Bob, ¿cómo estás?"
    else:
        return "Hola, ¿cómo estás?"
    

def menu():
    print ("1 saludar")
    print ("2 despedir")
    print ("3 calcular impuesto")
    print ("4 salir")



    opcion = input("Seleccione una opcion: ")

    nombre = input("Ingrese su nombre: ")

    while True: 
        match opcion: 
         case "1": 
            saludo(nombre)
         case "2": 
            despedida(nombre)
         case "3": 
              precio = float(input("Ingrese el precio: "))
              precio_total = calculo_impuestos(precio)

              print(f"El precio total con impuestos es: {precio_total}")
         case "4": 
            print("Saliendo...")
            break         
         case _:
            print("opcion invalida")

        opcion = input("Seleccione una opcion: ")

menu() # aca ya me tiene que saludar porque le enseñe como hacerlo 













