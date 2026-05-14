# print("SISTEMA DE BUSQUEDA")

# bodega = [
#     ["arroz", "frijoles", "lentejas"],
#     ["atun", "sardina", "sopa"],
#     ["agua", "jugo", "refresco"]
    
# ]

# # en que fila esta ?
# # en que columna esta dentro ?
# producto_buscado = bodega [1][1]
# print("Producto extraido: ", producto_buscado)


# # queremos sacar el agua 
# print("Bebida seleccionada", bodega[2][0])


# # modificar un dato si se acabo un producto y queremos poner otro 
# bodega[2][1] = "Te"
# print("Fila de bebidas actualizada: ", bodega[2])

# # --------------------------------------------------------------------------

# def mostrar_productos(estante):
#    # MUESTRA LOS PRODUCTOS
#     #ciclo externo. viaja por las filas completas (pisos)
#     for fila in estante: 
#     # ciclo interno, viaja por cada producto dentrro de la fila actual
#         for producto in fila: 
#             print("INVENTARIO: ", producto)

# print("INICIANDO INVENTARIO")

# estante = [
#     ["Pizza", "Pollo frito", "Lai Lai"],
#     ["agua", "Red bull", "modelo"]
# ]

# mostrar_productos(estante)
        
# for fila in estante: 
#     for producto in fila: 
#         if producto == "agua": 
#             fila[fila.index(producto)] = "vacio"
#             break
        
        
# print("="*15)

# mostrar_productos(estante)

# for fila in range (len(estante)): 
#     for columna in range (len(estante[fila])): 
#         if estante[fila][columna] == "vacio":
#             estante[fila][columna] = "pepsi"

# print("="*15)
# mostrar_productos(estante)

        # RETO
        # recorrer nuestro estante, encontrar agua y reemplazarlo por "vacio" y detener el ciclo 
        
        
#  # --------------------------------------------------------------------------

        
        
# print("INICIANDO INVENTARIO")
# print("\n- - - - - - - - - - -")



# estante = [
#     ["Pizza", "Pollo frito", "Lai Lai"],
#     ["Agua pura", "Red bull", "modelo"]
# ]

# encontrado = False 
# # usando el range y len nos ayuda a modificar nuestros valores externamente 
# for fila in range(len(estante)):  
#     # y lo volvemos usar internamente 
#     for producto in range(len(estante[fila])): 
#         if estante[fila][producto] == "Agua pura":
#             estante[fila][producto] = "vacio"  
#             encontrado = True
#             break  # salimos internamente 
    
#     if encontrado:
#         break  # salimos del todo 

# for fila in estante:
#     for producto in fila:
#         print("INVENTARIO |", producto)
#         print("- - - - - - - - - - -")
        
# #--------------------------------------------------------------------------        
        





