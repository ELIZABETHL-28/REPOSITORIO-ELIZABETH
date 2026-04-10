
# inventario basico de productos 
nombre_producto = "Camiseta"        #string
precio_producto = 19.99             # float    
cantidad_producto = 50              # int 
descuento = True                    # booleano 

#imprimir los valores y revisa5r que tipo son 
print("nombre del producto:", nombre_producto, "Tipo: ", type(nombre_producto))
print("Precio del producto:", precio_producto, "Tipo: ", type(precio_producto))
print("Cantidad del producto:", cantidad_producto, "Tipo: ", type(cantidad_producto))
print("Descuento del producto:", descuento, "Tipo: ", type(descuento))

# FORMA 1 convertir despues de preguntar 
cantidad = input("Cuantos cafes desea comprar?")
cantidad = int(cantidad)

# FORMA 2 convertir directamente al pedir el input
precio = float(input("cual es el precio del cafe ")) 

print("Cantidad de cafe:", cantidad, "Tipo: ", type(cantidad))
print("Precio del cafe:", precio, "Tipo: ", type(precio))

valor1 = 10 
valor2 = 3 

#division normal 
resultado = valor1 / valor2 #resultado es un float, aunque ambos valores sean entero. 5.0

#division entera
resultado = valor1 // valor2 #el resultado es in int, aunque ambos valores sean enteros, 5 

#modulo o resto de la division 
resto = valor1 % valor2 # resultado es un int, aunque ambos valores sean enteros. 

print("Resultado de la visicion", resultado)
print("Resultado de la visicion entera", resultado_entero)
print("Resultado de la visicion", resto)


#Caja registradora 


# %s: string
# %f: float
# %d: int

inventario = 8 
print(inventario > 5 )

print(inventario == 8)

name_pro1 = "Camiseta"
name_pro2 = "CAMISETA"

print(name_pro1 == name_pro2)


# # caja registradora
# print("Bienvenido a la tienda")
# nombre_producto = input("Ingrese el nombre del producto: ") # string
# precio_producto = float(input("Ingrese el precio del producto: ")) # float, se convierte directamente al pedir el input
# cantidad_producto = (input("Ingrese la cantidad del producto: ")) # int, se convierte directamente al pedir el input
# cantidad_producto = int(cantidad_producto) 

# # procesamiento de la información
# subtotal = precio_producto * cantidad_producto
# impuesto = subtotal * 0.15 # suponiendo un impuesto del 15%
# total = subtotal + impuesto

# # impresión de los resultados
# print("\n--- Resumen de la compra ---")
# # print("Nombre del producto:", nombre_producto)
# print("%25s: %10s" %("Nombre del producto", nombre_producto))
# # %s: string
# # %f: float
# # %d: int

# # print("Precio del producto:", precio_producto)
# print("%25s: %10.2f" %("Precio del producto", precio_producto))

# # print("Cantidad del producto:", cantidad_producto)
# print("%25s: %10d" %("Cantidad del producto", cantidad_producto))

# # print("Subtotal:", subtotal)
# print("%25s: %10.2f" %("Subtotal", subtotal))

# # print("Impuesto:", impuesto)
# print("%25s: %10.2f" %("Impuesto", impuesto))

# # print("Total:", total)
# print("%25s: %10.2f" %("Total", total))

#CAJA REGISTRADORA 
# print("BIENVENIDO A LA TIENDA")
# name_product = input("Ingrese el nombre del producto: ")
# price_product = float(input=("Ingrese el precio del producto: "))
# amount_product =  (input("Ingrese la cantidad del producto: "))
# amount_product = int(amount_product)

# # EN ESTA PARTE SE PROCESARA LA INFORMACION 
# subtotal = price_product * amount_product
# impuesto = subtotal * 0.15 #SUPONIENDO QUE ES EL 15%
# total = subtotal + impuesto

#IMPRESION DE LOS RESULTADOS TODAVIA FALTA CODIGO
