# EJERCICIO PRACTICO
#Han llegado 47 latas de atun queremos acomodarlas en estantes que solo soportan 10 latas cada estante
#cuantos estantes vamos a llenar por completo y cuantas nos van a sobrar para poner en exhibicion


print("TIENDA")
latas = int(input("CUANTAS LATAS HAY?: "))
estantes = int(input("LATAS POR ESTANTES DISPONIBLES: "))

valor1 = latas//estantes
valor2 = latas%estantes

print(f"Estanterias llenas: {valor1}")
print(f"Lastas sobrantes: {valor2}")
