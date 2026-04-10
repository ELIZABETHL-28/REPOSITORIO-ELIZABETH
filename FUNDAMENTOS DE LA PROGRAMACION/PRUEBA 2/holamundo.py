#saludo inicial de la tienda digital
print("Bienvenido a la tienda digital")
print("==============================")
# print("Que desea comprar?")

nombre_producto = input("Que desea comprar?")
edad_Cliente = input("Cual es tu edad?=")
# aguarda lo leido en nombre_producto

# OPCION 1 - dos print separados
print("El producto que escogio es: ", end="") #el end= es para evitar el salto de liena
print(nombre_producto)

# OPCION 2 determina una manera especial el print, uno solo con formato
print(f"el producto que escogio es: {nombre_producto}. Y la edad del cliente es: {edad_Cliente}")

# OPCION 3 un solo pront con concatenacion 
print("El producto que escogio es: " + nombre_producto)


print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
#Ejercicio de entrada y salida

print("==Queremos saber su opinion==")

pregunta_uno = input("Desea describir su producto favorito: ")
pregunta_dos = input("Que calificacion le das la tienda? (1-10): ")

print (f"El producto favorito es: {pregunta_uno}. Y que calificacion del servicio: {pregunta_dos}")
print ("QUE TENGA EXCELENTE DIA!")

print ("1. leche")
print ("2. cafe")
print ("3. arroz")

print ("1. leche\n2. cafe\n3. arroz")

print ("producto\t Precio")
print ("1. leche\t Q 2.50")
print ("2. cafe\t Q 2.50")
print ("3. arroz\t Q 2.50")


print ("producto\t Precio\t1. leche\t Q 2.50")
