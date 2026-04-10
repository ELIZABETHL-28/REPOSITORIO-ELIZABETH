class Camion: 
    pass 

class CentroLogistico: 
    pass 

camion1 = Camion()
camion2 = Camion()
camion3 = Camion()
camion4 = Camion()
camion5 = Camion()

garaje_principal = [
    camion1, 
    camion2, 
    camion3,
    camion4, 
    camion5
]

cantidad = len(garaje_principal)
print("CANTIDAD CAMIONES: ", cantidad)

impuesto_total = cantidad * 500
print("IMPUESTO TOTAL: ", impuesto_total)

print("\n\t(IDS)")
print("•••LISTAS DE CAMIONES•••")
for camion in garaje_principal: 
        print(id(camion))

print("\n•••CONTROLES DE CAPACIDAD•••")

if cantidad > 4: 
     print("'¡APACIDAD EXCEDIDA! DEBES MOVER CAMIONES A OTRA SUCURSAL")
else: 
     print("CAPACIDAD OPTIMA")