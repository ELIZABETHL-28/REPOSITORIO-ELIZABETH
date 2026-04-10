# ==========================================
#               EJERCICIO 1
# ==========================================
print("♦==♦ CONTROL DE ENTRADA AL TORNEO ♦==♦")

nombre = input("INGRESE EL NOMBRE DEL PARTICIPANTE: ")
persona = int(input("INGRESE EDAD DE LA PERSONA: "))
entrada = input("¿INSCRIPCION CONFIRMADA? (si/no): ") == "si"

if persona >= 15 and entrada: 
    print("PARTICIPANTE AUTORIZADO A INGRESAR")
else: 
    print("PARTICIPANTE NO AUTORIZADO")

print("=== EXCELENTE DIA ===")



# ==========================================
#               EJERCICIO 2
# ==========================================
print("♦==♦ BATERIA DE CELULAR ♦==♦")

bateria = int(input("Ingrese el porcentaje de batería: "))
if bateria <= 20:
    print("Debe cargar el celular")
else:
    print("Batería suficiente")



# ==========================================
#               EJERCICIO 3
# ==========================================
print("♦==♦ CLASIFICACION DE ENVIO ♦==♦")

peso = float(input("PESO (Kg): "))

if peso < 1:
    print("PAQUETE LIVIANO")

elif peso  <= 5:
    print("PAQUETE ESTANDAR")

else:
    print("PAQUETE PESADO")



# ==========================================
#               EJERCICIO 4
# ==========================================
print("♦==♦ SEMAFORO ♦==♦")

color = input("Ingrese el color del semáforo: ")
if color == ("verde"):
    print("Avanzar")
elif color == ("amarillo"):
    print("Precaución")
else:
    print("Detenerse")



# ==========================================
#               EJERCICIO 5  
# ==========================================
print("♦==♦ ACCESO VIP A CONCIERTO CON COMPRA DE BEBIDA ♦==♦")
# un sistema de conciertos desea validar si una persona puede entrar al area VIP 

cliente = input("NOMBRE DEL CLIENTE: ")
edad = int(input("INGRESE EDAD DE LA PERSONA: "))
entrada = input("¿PROVEE ENTRADA? (General/VIP): ")
plata = float(input("DINERO DISPONIBLE: "))
bebida = float(input("PRECIO DE BEBIDA ESPECIAL: ")) 

if entrada == "vip" and edad >= 18:
    print("ACCESO VIP APROBADO PARA>: ", cliente) 
    desea_bebida = input("DESEA COMPRAR LA BEBIDA ESPECIAL (si/no): ")

    if desea_bebida == "si": 
         if plata >= bebida:
             restante = plata - bebida
             print("BEBIDA ESPECIAL APROVADA")
             print("CAMBIO: ", restante)

    else: 
        print("NO TIENE DINERO SUFICIENTE PARA BEBIDA ESPECIAL!")

else: 
   print("NO PUEDE ENTRAR AL AREA VIP")





# ==========================================
#               EJERCICIO 6
# ==========================================
print("♦==♦ BECAS ESTUDIANTILES (POR PROMEDIO Y CONDICION ECONOMICA) ♦==♦")

estudiante = input("NOMBRE DEL ESTUDIANTE: ")
promedio = float(input("INGRESE SU PROMEDIO: "))
ingreso = int(input("INGRESO FAMILIAR MENSUAL: "))
materias = int(input("CANTIDAD DE MATERIAS APROVADAS: "))

#RESULTADO
resultado = " "
monto = 0

#REGLAS

if promedio < 70:
    resultado= "BECA NO APROVADA"
    monto = 0

elif promedio >=70 and promedio <=84:
    if ingreso <= 400000:
        resultado = "BECA PARCIAL"
    else:
        resultado = "BECA NO APROVADA"
        monto = 0  
elif promedio >= 85:
    if materias >=5 and ingreso <= 400000:
        resultado = "BECA COMPLETA"
        monto = 100000
    else: 
        resultado = "BECA PARCIAL"
        monto = 50000
    print("\n=======================")
    print("BECA COMPLETA: 100000 ")
    print("BECA PARCIAL: 50000 ")
    print("SIN BECA: 0 ")
    print("=======================")


print("\nESTUDIANTE: ", estudiante)
print("RESULTADO: ", resultado)
print("MONTO ASIGNADO: ", monto)




# ==========================================
#               EJERCICIO 7
# ==========================================
print("♦==♦ TARIFA DE HOTEL CON RECARGO Y DESCUENTO ♦==♦")

cliente = input("NOMBRE DEL CLIENTE: ")
temporada = input("TEMPORADA: (ALTA, MEDIA O BAJA): ")
noches = int(input("CANTIDAD DE NOCHES: "))
precio = float(input("PRECIO BASE POR NOCHE "))
membresia = input("¿TIENE MEMBRESIA? (si/no): ") 

subtotal = precio * noches 
descuento = 0


if temporada == "alta": 
    subtotal = subtotal * 1.20
elif temporada == "media": 
    subtotal = subtotal * 1.10
else: 
    temporada == "baja"
    print("NO APLICA RECARGO")

if membresia == "si" and noches >= 3:
    descuento = subtotal * 0.15
elif membresia == "si" or noches == 2:
    descuento = subtotal * 0.05   

total = subtotal * descuento

print ("---------------------------------------------")

print("CLIENTE: ", cliente)
print("SUBTOTAL CON RECARGO: ", subtotal)
print("DESCUENTO APLICADO: ", descuento ("%"))
print("TOTAL FINAL: ", total)

print ("---------------------------------------------")



# ==========================================
#               EJERCICIO 8
# ==========================================
print("♦==♦ ACADEMIA CON PERMISOS ♦==♦")
print("1 matricular")
print("2 notas ")
print("3 certificado")
print("4 salir")

opcion = input("Seleccione (1-4) o escriba salir ")
usuario = input("Usuario: (admin, profesor, estudiante) ")
promedio = int(input("Promedio: "))

match opcion:
    case "matricular" | "1":
        if usuario == "admin" or usuario == "profesor":
            print("MATRICULA REALIZADA")
        else: 
            print("NO TIENE PERMISOS")

    case "notas" | "2": 
        if usuario == "profesor" or usuario == "estudiante":
            print("NOTAS GENERADAS")
            print("ACCESO PERMITIDO A PROFESOR Y ESTUDIANTES")
        else: 
            print("NO TIENE PERMISOS")
        
    case "certificado" | "3": 
        if usuario == "estudiante" and promedio >=70:
            print("CERTIFICADO GENERADO CORRECTAMENTE")
        else: 
            print("NO TIENE PERMISOS")

    case "salir" | "4":
        print("Saliendo...")

    case _:
        print("Opción inválida")



# ==========================================
#               EJERCICIO 9
# ==========================================
print("♦==♦ TIENDA GAMER CON PROMOCIONES ♦==♦")

cliente = input("NOMBRE DEL CLIENTE: ")
producto = input("PRODUCTO: ")
precio = float(input("PRECIO UNITARIO: "))
cantidad = int(input("CANTIDAD DESEADA: "))
stock = int(input("CANTIDAD DE EXISTENCIAS: "))
membresia = input("TIENE MEMBRESIA GAMER (si/no): ") == "si"

if cantidad > stock: 
    print("NO SE PUDE HACER LA VENTA")

else: 
    subtotal = precio * cantidad
    descuento = 0 

    if subtotal > 50000 and membresia: 
        descuento = subtotal * 0.20
    elif subtotal > 30000 or membresia: 
        descuento = subtotal * 0.10 

        total = subtotal - descuento

        print ("\n---------------------------------------------")
        print("VENTA APROVADA")
        print("CLIENTE: ", cliente)
        print("PRODUCTO: ", producto)
        print("SUBTOTAL: ", subtotal)
        print("DESCUENTO: ", descuento)
        print("TOTAL FINAL: ", total)
        print ("---------------------------------------------")



# ==========================================
#               EJERCICIO 10
# ==========================================
print("♦==♦ MISIONES Y CALCULO DE RECOMPENSA ♦==♦")

print("BIENVENIDO JUGADOR")
print("1 bosque ")
print("2 castillo")
print("3 dragon")
print("3 salir")

jugador = input("NOMBRE JUGADOR: ")
clase = input("CLASE DE JUGADOR: (guerrero, mago, arquero) ")
opcion = input("OPCION DE MISION  ")
nivel = int(input("NIVEL: "))
enemigos = int(input("CANTIDAD DE ENEMIGOS DERROTADOS: "))

if opcion == "1" or opcion == "bosque":
    if nivel >= 1:
        recompensa = enemigos * 10
        print("MISION BOSQUE COMPLETADA")
        print("RECOMPENSA: ", recompensa)

elif opcion == "2" or opcion == "castillo": 
    if nivel >= 5:
        recompensa = enemigos * 20
        bono = 0
        if clase == "guerrero" or clase == "mago":
            bono = 50
        total = recompensa + bono
        print ("---------------------------------------------")
        print("MISION CASTILLO COMPLETADA")
        print("RECOMPENSA BASE: ", recompensa)
        print("BONO ADICIONAL: ", bono)
        print("RECOMPENSA TOTAL: ", total)
        print ("---------------------------------------------")
    else: 
        print("INSUFICIENTE EN NIVEL CASTILLO")

elif opcion == "3" or opcion == "dragon": 
    if nivel >= 10 and (clase == "guerrero" or clase == "arquero"):
        recompensa = enemigos * 50
        bono = 0

        if enemigos >3:
            bono = 100
        total = recompensa + bono
        print ("---------------------------------------------")
        print("MISION DRAGON COMPLETADA")
        print("RECOMPENSA BASE: ", recompensa)
        print("BONO ADICIONAL: ", bono)
        print("RECOMPENSA TOTAL: ", total)
        print ("---------------------------------------------")
    else: 
        print("INSUFICIENTE EN NIVEL DRAGON")

elif opcion == "4" or opcion == "salir": 
    print("saliendo del juego")

else:
    print("OPCION INVALIDA PORQUE NO CUMPLE CON LOS REQUISITOS A PEDIR")
    print("(POSIBLEMENTE NO ESTA AL NIVEL Y NO CUMPLIENDO CON LOS REQUISITOS)")



print("SIGUE SIENDO UN INCREIBLE JUGADOR")



# FIN DE LABORATORIO 











