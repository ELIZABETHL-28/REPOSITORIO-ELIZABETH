#FACTURA INVENTARIO

print("↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨")
print("          |INVENTARIO|")
print("↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨")

#CREACION DE PRODUCTOS

things1 = input ("NOMBRE DEL PRODUCTO: ")
price1 = input ("PRECIO DEL PRODUCTO: ")
amount1 = input ("CANTIDAD DEL PRODUCTO: ")

things2 = input ("NOMBRE DEL PRODUCTO: ")
price2 = input ("PRECIO DEL PRODUCTO: ")
amount2 = input ("CANTIDAD DEL PRODUCTO: ")

things3 = input ("NOMBRE DEL PRODUCTO: ")
price3 = input ("PRECIO DEL PRODUCTO: ")
amount3 = input ("CANTIDAD DEL PRODUCTO: ")

print ("\t   FACTURA DEL INVENTARIO")
print("↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨")
print("PRODUCTO \t| PRECIO \t| CANTIDAD")
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
print(f"{things1:10s}\t| Q.{price1:5s}\t| {amount1:5s}")
print(f"{things2:10s}\t| Q.{price2:5s}\t| {amount2:5s}")
print(f"{things3:10s}\t| Q.{price3:5s}\t| {amount3:5s}")
