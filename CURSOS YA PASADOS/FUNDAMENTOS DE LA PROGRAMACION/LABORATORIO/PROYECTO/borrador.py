print("\t\tPROYECTO")
print("\tLA LINEA DE PRODUCCION")
print("PRODUCTOS AGROINDUSTRIALES COMODIN S.A.\n")

# nombres de los productos y almacenar nuestros datos
tipos_de_producto = ["Fertilizante", "Insecticida", "Herbicida"]

lotes = [0, 0 , 0], 
producto = [0, 0 , 0] 
promedios = [0, 0, 0]

# VAMOS A DEFINIR QUE FUNCIONES QUEREMOS HACER 
# llevaremos cuantro tipos de categorias 
def categorias(promedio): 
    if promedio <= 99: 
        return(print("Insuficiente"))
    elif promedio <= 299:
        return(print("Regular"))
    elif promedio <= 599:
        return(print("Idoneo"))    
    else:
        return(print("Sobreproduccion")) 
    
# codigo para procesar un lote 
def procesar_lote(digitos): 
    codigo = int(digitos(0))-1
    cantidad = int(digitos(1-4))
    
    lotes(codigo) += 1 
    digitos[codigo] += cantidad
    
# codigo para calculo de promedios por producto 
def calculo_de_promedios():
    for valor in range(3):
       if lotes[valor] > 0: 
        promedios[valor]= producto[valor] /lotes[valor]
        
# funciones para la tabla 
