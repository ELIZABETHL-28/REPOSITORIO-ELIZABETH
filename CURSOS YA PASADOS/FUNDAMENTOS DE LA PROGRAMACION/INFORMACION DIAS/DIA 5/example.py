# # RETO 
# ### Reto 1: La Tabla de Multiplicar 
# # Instrucción: El gerente necesita calcular precios al por mayor. Pide al usuario que ingrese un número (ejemplo: 7),
# # para imprimir la tabla de multiplicar de ese número del 1 al 10.

# number = int(input("INGRESE UN NUMERO: "))

# for a in range(1, 10): 
#     result = number * a 
#     print(number, "X", a, "=", result)


# # Reto 2: La Meta de Ahorro de la Tienda (Uso de 'while')
# # Instrucción: La tienda quiere comprar un nuevo rótulo luminoso que cuesta 100,000 dólares.
# #  Crea un programa que tenga una meta de 100000 y un ahorro que empiece en 0. 
# # Usa un bucle para preguntarle al gerente: "¿Cuánto dinero depositamos hoy a la cuenta de ahorros?". 
# # Suma eso al ahorro total. El bucle debe repetirse *mientras* el ahorro sea menor a la meta.
# #  Al salir del bucle, felicita al gerente.


# meta = 100
# saving = 0 

# while saving < meta: 
#     deposit = float(input("¿CUANTA PLATA DEPOSITAS HOY?: "))
#     saving += deposit 
#     print ("AHORRO TOTAL: ", saving)

# print ("FELICIDADES! VAS CRECIENDO ECONOMICAMENTE")



# EJEMPLO DE DIA 5

# while True: 
#     name = input("INGRESE SU NOMBRE... (sale para terminar): ")

#     if name == "salir": 
#         break 

#     print("BIENVENIDO, ", name)


# print ("PROGRAMA FINALIZADO")

# SEGUNDO EJEMPLO
# for product in range (6): 
#     if product == 3: 
#         continue
#     print("PRODUCTO ETIQUETADO: ", product)





# -----------------------------------------------------------------------------





# print ("="*15)
# print("ESCANER DE PRODUCTO")
# print ("="*15)

# #EJjemplo de un BREAK buscando un porducto peligroso
# for caja in range (1, 11):
#     print(f"escaneando caja {caja}")

#     if caja == 5:
#         print("ALERTA!!! Producto peligroso encontrado, deteniendo escaneo")


# print ("EL ESCANER HA TERMINADO SU REVISON DE SEGURIDAD")



# #ejemplo de un CONTINUE ignorando errores

# print ("\n"+"="+15)
# print("PROCESO DE PAGOS")
# print ("="+15)

# for cliente in range (1, 6): 
#     print(f"PROCESANDO PAGO DEL CLIENTE {cliente}")

#     #simulamos que el cliente 5 tiene un error en su pago
#     # fondos insuficientes, tarjeta vencida, etc
#     if cliente == 5:
#         print("ERROR! pago no procesado, saltando al siguiente cliente")
#         continue 

#     print("PAGO PROCESADO EXITOSAMENTE")

# -----------------------------------------------------------------------------


# mi_lista = [10, "hola", 3.14 ]


# ### forma 2: sin elementos 
# lista_vacia = []

# ## ACCEDER A LOS ELEMENTOS 
# #PARA QUE SIRVE LOS INDICES, 
# #### LAS LISTAS TAMBIEN EMPEZAN DESDE 0
# ### dos pasos
# saludo = mi_lista [1] 
# print (saludo)

# ### un paso
# print (mi_lista[1])

# ## agregar elementos (`append`)
# ### sintaxis 
# # `nombre de la lista` + `.` + `append` + `lo que quiere agregar` + `J`

# lista_vacia.append ("Diego")

# print (lista_vacia[0])

# mi_lista.append("mundo")
# print(mi_lista)

# # recorrer una lista
# # forma 1: con un ciclo for
# for elemento in mi_lista:
#     print(elemento)

#     if elemento == 3.14: 
#         print("encontre el numero pi")
#         break

# # forma 2: usando los indices 
# #len(mi_lista) # devuelve la cantidad de elementos que tiene la lista
# for indice in range (len(mi_lista)):
#     print(mi_lista(indice))


# print(mi_lista[1:3])

# print(mi_lista[0:4:2])

# mi_lista [1] = "HOLA"
# print(mi_lista)

# mi_lista.remove(10)
# print(mi_lista)

# -----------------------------------------------------------------------------


# # --- lista de 3 platillos ---
# menu = ["FRUTTI DI MARE", "SANTA FE", "FIORENTINA"]
 
# print("- - - - - - - - - - - - - - -")
# print("Segundo platillo:", menu[1])
# print("- - - - - - - - - - - - - - -")

# print("\n== Menú completo:==")
# for platillo in menu:
#     print(platillo)




# # --- creacion de tupla ---

# producto = ("Arroz", 1200, 5)

# # imprimir usando indices
# print("Nombre: ", producto[0])
# print("Precio: ", producto[1])
# print("Cantidad: ", producto[2])

# total = producto[1] * producto[2]
# print("VALOR TOTAL DEL PRODUCTO: ", total)

# # con esto queremos cambiar el valor del producto
# producto[1] = 1250 
    