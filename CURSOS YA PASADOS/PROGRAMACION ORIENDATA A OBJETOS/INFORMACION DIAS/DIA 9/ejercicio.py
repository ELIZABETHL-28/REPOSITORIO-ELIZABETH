with open("registro.txt", "r") as prueba:
    contador = 0 

    
    for linea in prueba: 
        print(linea.strip())
        contador += 1
        
print(f"TOTAL DE LINEAS LEIDAS: {contador}") 


prueba.close()
    