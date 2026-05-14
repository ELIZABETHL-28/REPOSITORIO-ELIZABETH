# producto = {
#     "nombre": "Arroz", 
#     "precio": 1200,
#     "cantidad": 5
# }

# print(producto["nombre"])
# print(producto["precio"])
# print(producto["cantidad"])

# total = producto["cantidad"] * producto["precio"]
# print(f"el total de los productos son: {total}")
# print(producto)

# #modificar
# producto["precio"] = 1500.1
# print(producto)

# producto["cantidad"] = producto["cantidad"] - 1
# print(producto)

# #agregar si no existe
# producto["categoria"] = "Granos"
# print(producto)


# # el for recorre todo el diccionario 
# # clave en esta caso se refiere a nombre, precio, cantidad y categoria 
# # y clave le dice a producto que el va a tomar su valor y saldra al valor ya sea
# # arroz, 4, 1500.1
# for clave in producto: 
#     print(f"clave: {clave}: valor: {producto[clave]}") 
    
    
    
# for clave, valor in producto.items(): 
#     print(f"Calve: {clave}: valor: {valor}")
    

def mostrar_inventario(productos): 
    
    # forma 1
    print("FORMA 1")
    for num_articulo in range (len(productos)):
        print(productos[num_articulo]["nombre"])
        print(productos[num_articulo]["precio"])
        print(productos[num_articulo]["cantidad"])
        
    print("FORMA 2")   
    # forma 2  
    for num_articulo in range (len(productos)):
        # float a str: 100.5 -> "100.5"
        articulo = productos[num_articulo]["nombre"] + "-" + str(productos[num_articulo]["precio"]) + "-" + str(productos[num_articulo]["cantidad"])
        print(articulo)
        
    print("FORMA 3")    
    # forma 3 
    for num_articulo in range (len(productos)): 
        print
        
    print("FORMA 4")   
    # forma 4 
    for num_articulo in range (len(productos)):
        print(productos[num_articulo]["nombre"], end = "-")
        print(productos[num_articulo]["precio"], end = "-")
        print(productos[num_articulo]["cantidad"])


productos = []

while True: 
    nombre = input("ingrese el nombre del producto o FIN para terminar ")
    if nombre == "FIN": #Todo: mejorar validacion 
        mostrar_inventario(productos)
        break
    
    precio = float(input("Ingresee el precio de productos")) #str a float 
    cantidad = int(input("Ingresee el cantidad de productos")) # str a int

        
    productito = {
        "nombre": nombre, 
        "precio": precio, 
        "cantidad": cantidad
    }
    
productos.append(productito)
   
