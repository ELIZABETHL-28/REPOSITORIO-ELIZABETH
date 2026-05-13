# # - - - - - - - - - - - - - - - - - -  
# def mensaje_bienvenida(): 
#     print("Bienvenido al sistema de ventas ! ")
#     print("Esperamos que tenga una excelente compra")

# mensaje_bienvenida()

# # - - - - - - - - - - - - - - - - - -  
 
# def saludar_cliente(nombre): 
#     print("Hola!")
#     print(f"{nombre}, bienvenido al gimnasio")

# nombre = input("ingrese su nombre: ")

# saludar_cliente(nombre)

# # - - - - - - - - - - - - - - - - - -  

# def calcular_total(precio, cantidad):
#     total = precio * cantidad
#     return total

# precio = float(input("Ingrese el precio del producto: "))
# cantidad = int(input("Ingrese la cantidad comprada: "))

# total_final = calcular_total(precio, cantidad)

# print("El total a pagar es:", total_final)

# # - - - - - - - - - - - - - - - - - -  

# def calcular_fichas(dinero, precio_ficha):
#     fichas = dinero // precio_ficha
#     vuelto = dinero % precio_ficha
#     return fichas, vuelto

# precio_ficha = 500

# while True:
#     print("\n--- MENÚ ---")
#     print("1 - Comprar fichas")
#     print("2 - Salir")

#     opcion = input("Seleccione una opción: ")

#     if opcion == "1":
#         nombre = input("Ingrese su nombre: ")
#         dinero = int(input("Ingrese cuánto dinero tiene: "))

#         fichas, vuelto = calcular_fichas(dinero, precio_ficha)

#         if fichas == 0:
#             print(f"{nombre}, no tiene dinero suficiente para comprar una ficha.")
#         else:
#             print(f"\nCliente: {nombre}")
#             print(f"Cantidad de fichas que puede comprar: {fichas}")
#             print(f"Dinero de vuelto: {vuelto}")

#     elif opcion == "2":
#         print("Gracias por usar el sistema.")
#         break

#     else:
#         print("Opción inválida, intente nuevamente.")



# # - - - - - - - - - - - - - - - - - -  
##RETO 1 DIA 6
# def es_mayor_de_edad(edad): 
#     if edad >= 18:
#         return True
#     else:
#         return False 

# years_user = int(input("INGRESE SU EDAD: "))

# resultado = es_mayor_de_edad(years_user)

# if resultado: 
#     print("PUEDES COMPRAR ALCOHOL")
# else: 
#     print("=VENTA DENEGADA=")
    
# # - - - - - - - - - - - - - - - - - -  

##RETO 2 DIA 6

# def aplicar_descuento (precio, porcentaje_descuento):
#     descuento = precio * (porcentaje_descuento/100)
#     nuevo_precio = precio - descuento
#     return nuevo_precio 

# precio_final = aplicar_descuento(5000, 20)
# print("El precio final es: ", precio_final)

    
    
    
    
