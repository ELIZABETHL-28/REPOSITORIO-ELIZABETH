# DIA 2 - SEGUNDA SEMANA  
# REPASO 
* tipos de datos 
* operadores aritmeticos (+, *, /, -)
* tipos de operaciones especiales (modulo (%), division entera (//))
* operadores logicos (and, not, or)
* operadores comparativos( <, >, ==, >=, <=, !=) 
 ### el = siempre va en segundo lugar 
* casting: int(), float(), str()



# LA REGLA BASICA: 
#### Python es estricto con los bloques 
EL `if`: 
Bloque condicional del if 
    me indica que esto le pertenece al blque
    esto tambien le pertenece 

Bloque condicional del if 
    me indica que esto le pertenece al blque
    esto tambien le pertenece 

#### importante que la condicional... 

## SINTAXIS
```python
if condicion: (los dos puntos dice )
    accion 
```
## ejemplo
```python
dinero = 1000
precio = 750

if dinero >= precio: 
    print("Venta aprobada")
```

# PRACTICA GUIADA 
programar un sistema de acceso a la bodega de la tienda: 
```python
print("=== SISTEMA DE SEGURIDAD DE LA BODEGA ===")

clave_ingresar = input("Ingrese la clave de seguridad: ")
clave_correcta = "1234"

if clave_ingresar == clave_correcta: 
    print("Clave correcta. Acceso permitido.")
    print("Bienvenido a la bodega super segura.")

print("Fin del programa")

```

# CONDICIONAL
El `else`: 
* NO LLEVA UNA CONDICION A LADO 
* ES EL BASURERO QUE RECOGE CUALQUIER COSA QUE NO SE HAYA CUMPPLIDO CON LA REGLA DEL `if`


## EJEMPLO 
```python
dinero = float(input("Dinero del cliente: "))
precio = 1200

if dinero >= precio: 
    print("puede comprar el producto")
else: 
    print ("no puede comprar el producto")

```


### EJERCICIO 
Un cine desea automatizar una parte de su sistema de control de acceso 
El sistema debe de verificar si uuna persona puede ingresar a una pelicula para mayores de edad 

El programa debe de solicitar al usuario: 
-  edad de la persona 
- si posee entrada comprada (responder un si o no )

 SI LA PERSONA TIENE 18+ Y TIENE ENTRADA PUEDE INGRESAR A LA PELICULA, EN CASO CONTRARIO, NO SE PERMITE LA ENTRADA. 

```python
print("♦♦♦ ACCESO AL CINE ♦♦♦")

persona = int(input("INGRESE EDAD DE LA PERSONA: "))
entrada = input("¿PROVEE ENTRADA? (si/no): ") == "si"

if persona >= 18 and entrada: 
    print("Acceso permitido")
else: 
    print("NO PUEDE INGRESAR")

print("EXCELENTE DIA")

```

# CONDICIONAL `elif` es abreviatura del `else` e `if`

## EJEMPLO 
```python
edad = int(input("Digite su edad: "))
precio_entrada = 2000

if edad <= 12: 
    print("el cliente es un nino, tiene un descuento del 50%")
    total = precio_entrada * 0.5
elif edad >= 60: 
    print("el cliente es un adulto mayor, tiene un descuento del 25%")
    total = precio_entrada * 0.75
else: 
    print("el cliente es un adulto, no tiene descuento")
    total = precio_entrada

print("El precio total de la entrada es: ", total)
```

## EJERCICIO 
#### El control de Inventario 
**INSTRUCCIONES**
Escribe un programa que pida la cantidad de cajas de disponibles en la bodega. 

* si la cantidad es mayor a 20, imprime "Inventario saludable"
* Si la cantidad esta entre 1 y 20, imprime "ALERTA: Hacer pedido al proveedor "
* Si la cantidad es exactamente 0, imprime "Urgente: producto agotado". 


```python
print("♦♦♦CONTROL DE INVENTARIO♦♦♦")

milk = int(input("CANTIDAD-CAJAS DE LECHE DISPONIBLES: "))

if milk > 20:
    print("INVENTARIO SALUDABLE")

elif milk  > 0:
    print("ALERTA: HACER PEDIDO AL PROVEEDOR")

else: 
    print("URGENTE: PRODUCTO AGOTADO")


```


### condicional: switch (match/case)


```python
opcion = input ("seleccione (1-3)")

if opcion == "1": 
    print("registrando producto...")
elif opcion == "2": 
    print("mostrando inventario... ")
elif opcion == "3": 
    print("saliendo...")
else: 
    print(" opcion valida...")

```

`match/case` es una estructura de seleccion multiple que compara un valor contra varios "casos" y eecuta el bloque correspondiente 

### sintaxis 
```python
match valor: 
    case patron1: #acciones 
    
    case patron2: #acciones
    
    case _: #acciones por defecto

```
## ejemplo: 
```python
opcion = input ("selecione (1-3): ")

match opcion:
    case "1":
        print("registrando producto...")
        ### ACA YA PODEMOS IR AGREGANDO IF, ELIF Y ELSE ADEMAS CON OPERADORES 
    case "2":
        print("mostrando inventario")
    case "3":
        print("saliendo...")
    case _:
        print("opcion valida")
```

##### PYTHON EXIGE EL ORDEN 

# OPERADORES: 

`and` y el 
 `or`= `|` 

 ## ejemplo: 
```python
opcion = input ("selecione (1-3) o escriba salir ")

match opcion:
    case "1":
        print("registrando producto...")
        ### ACA YA PODEMOS IR AGREGANDO IF, ELIF Y ELSE ADEMAS CON OPERADORES 
    case "2":
        print("mostrando inventario")
    case "3" | "salir":
        print("saliendo...")
    case _:
        print("opcion valida")
```


## CUANDO USAR MATCH/CASE VS IF/ELIF/ELSE
## USAR MATCH/CASE CUANDO: 
    - Hay muchas opciones claras (menu)
    - Si quiere leer el codigo mas rapido
    - se agrupan varias opciones en un caso

## USAR IF/ELIF/ELSE
    - Hay pocas opciones
    - la logica es mas matematica o basada en rangos
    - no se tiene python 3.10+ disponible. 




