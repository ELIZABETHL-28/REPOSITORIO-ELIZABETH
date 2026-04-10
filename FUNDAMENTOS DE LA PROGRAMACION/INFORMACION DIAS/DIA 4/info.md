# NUEVO DIA - NUEVOS CONOCIMIENTOS
## TAREAS REPETITIVAS - CICLOS
 * for, while  
 print ("1")
 print ("2")
 print ("3")

 ### CICLO CON CONDICION `while`  (mientras)

El bucle while repite un bloque de codigo mientras una condicion sea verdadera. En el instante en que la condicoin se vuelve falsa, el ciclo termina 

## sintaxis 
 ```python
 while condicion:

 ```
# EJEMPLO 1
```python
contador = 1

while contador <= 3: 
    print ("HOLA, SOY EL CICLO WHILE")
    print("contador: ", contador)
    valor = float(input("ingrese un numero pequeno de aumento:"))
    contador = contador + valor

 ```

 # EJEMPLO 2
```python
clave_true = "1234"

intento = ""

while intento != clave_true: 
    intento = input("INGRESE LA CLAVE: ")

print("CLAVE CORRECTA! ACCESO CONCEDIDO")

 ```

  # EJEMPLO 3
```python
opcion = ""

while opcion != "salir" and opcion != "2":
    print(" 1 - saludar")
    print(" 2 - salir")
    opcion = input("INGRESE UNA OPCION: ")

    if opcion =="1" or opcion == "saludar":
        print("HOLA, COMO ESTAS?")
    elif opcion == "2" or opcion == "salir": 
        print("ADIOS, BUEN DIA")
    else:
        print("OPCION NO VALIDA. INGRESE UNA VALIDA")LAVE CORRECTA! ACCESO CONCEDIDO")
 ```

 # CICLO POR CONTADOR `for` (para) cuando sabemos exactamente la cantidad 

 `range(cantidad)` 

 ## EJEMPLO forma 1: range(cantidad) 

 ```python
 #0, 1, 2, 3, 4 NO LLEGA AL 5 PORQUE 0 OCUPA EL ESPACIO 
 # 0 .... N - 1
 # POR DEFECTO ME VA A INICIAR EN 0 Y ME VA INCREMENTAR DE 1 EN 1
for index in range(5):
    print (index)
 ```

 ## EJEMPLO forma 2 : range( inicio, cantidad) 

 ```python
# 0, 1, 2, 3, 4 NO LLEGA AL 5 PORQUE 0 OCUPA EL ESPACIO 
 # 1 .... N - 1
 # POR DEFECTO ME VA A INCREMENTAR DE 1 EN 1 
for index in range(1, 5):
    print (index)
 ```

 ## EJEMPLO forma 3: range(inicio, cantidad, incremento) 

 ```python
 # 1, 3, NO CON AL 5  
 # 0 .... N - 1


for index in range(1, 5, 2):
    print (index)
 ```

# EJEMPLO ESCANEAR N PRODUCTOS
 ```python
for no_turno in range(5):
    print ("BEEP: producto escaneado: (turno es:", no_turno + 1, ")")
 ```
# EJEMPLO LIMPIADOR DE PASILLOS PARES
  ```python
for pasillo in range(0, 10, 2):
    print ("LIMPIANDO EL PASILLO: ", pasillo + 2)
 ```

 # EJEMPLO TOTAL CARRITO DE COMPRAS
   ```python
total = 0.0

for articulo in range (4):
    precio = float(input("ingrese el precio del articulo: "))

    # ttal = total + precio 
    total += precio

print("EL TOTAL A PAGAR ES: ", total)
 ```

