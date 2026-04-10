# TIPOS DE DATOS 
* string: es de tipo texto. Cualquier caracter (letras, numeros o simbolos ) que este encerrado entre ""/¨¨

* entero, (integer) (`int`): numero enteros, sin decimales 

* flotantes. (`float`): numero con decimales 

* booleanos (`bool`): solo tiene 2 opciones, guardar un valor verdadero o falso. Apagada o encendida `True` or `False`

## ejemplo 
### inventario basico de productos 

```Python 
# inventario basico de productos 
nombre_producto = "Camiseta"        #string
precio_producto = 19.99             # float    
cantidad_producto = 50              # int 
descuento = True                    # booleano 

#imprimir los valores y revisa5r que tipo son 
print("nombre del producto:", nombre_producto, "Tipo: ", type(nombre_producto))
print("Precio del producto:", precio_producto, "Tipo: ", type(precio_producto))
print("Cantidad del producto:", cantidad_producto, "Tipo: ", type(cantidad_producto))
print("Descuento del producto:", descuento, "Tipo: ", type(descuento))
```

# Casting (casteo de datos)
Convierte un string a su equivalencia numerica 
Herramientas de conversion: 
* `int()`: string a entero 
* `float()`:  string a flotante 


```
# FORMA 1 convertir despues de preguntar 
cantidad = input("Cuantos cafes desea comprar?")
cantidad = int(cantidad)

# FORMA 2 convertir directamente al pedir el input
precio = float(input("cual es el precio del cafe ")) 

print("Cantidad de cafe:", cantidad, "Tipo: ", type(cantidad))
print("Precio del cafe:", precio, "Tipo: ", type(precio))

```

# Operadores aritmeticos 
suma 
Resta 
multiplicacion 
division 

Ej: resultado = valor1 / valor2

## operadores especiales 
// (division entera)
% (modulo)

# EJEMPLO 

#### Caja registradora 
```
print("Bienvenido a la tienda")
 name_produ = input("Ingrese el nombre del producto: ") #string
 price = float(input("Ingrese el precio del producto: ") )#string
 amount = (input("Ingrese el cantidad del producto: ") )#string
 amount = int(amount) #string


#procesamiento de los resultado 
print("\n ---- RESUMEN DE LA COMPRA")

# IMPRESION DE DATOS





# %s: string
# %f: float
# %d: int

```


# EJERCICIO PRACTICO 
Han llegado 47 latas de atun queremos acomodarlas en estantes que solo soportan 10 latas cada estante

cuantos estantes vamos a llenar por completo y cuantas nos van a sobrar para poner en exhibicion 

```Python

cantidad = input("Cuantas latas hay?  ")
print("CANTIDAD DE LATAS: ", cantidad)
estantes = input("CUANTO ESTANTES DISPONIBLES: ")
cantidad = float(input("cuantas latas sobran? ")) 


valor1 = 47
valor2 = 10 

resultado = valor1 - valor2 

```



# OPERADORES DE COMPARACION 
`==` (Igual que) son exactamente igual?

* ATENCION: deben enfatizar la diferencia un = es para guardar en la caja (asignacion); Dos  == son para preguntar (Comparacion)


* != (Diferencian de) Son distintos? 
* < Menor que   > Menor que 
* < Menos o igual que    >Mayor o igual que 

EJEMPLO 

inventario = 8 
print(inventario > 5 )

print(inventario == 8)

name_pro1 = "Camiseta"
name_pro2 = "CAMISETA"

print(name_pro1 == name_pro2)


```Python

manzanas = 5
precio_apples = 500

print("--- REPORTE ---")

### tenemos mas de 10 manzanas? 

hay_apples = manzanas > 10
print("Hay mas de 10 manzanas? ", hay_apples)

### nos quedamos sin stock en la bodega?
sin_stock = manzanas == 0 
print(f"Nos quedamos sin stock en la bodega? {sin_stock}")

#comparacion de nombre de productos
producto_buscado = "Manzana"

es_manzana = manzanas == producto_buscado 
print(f"El producto buscado esta en bodega" {es_manzana})

## La diferencia entre = y == es que el 2 se encarga de comparar ej: buscamos Manzana y tenemos de opcion manzana y Manzana 

```


# OPERADORES LOGICOS 
AND 
OR 
NOT 

# EJERCICIO 

```Python

print(""Bienvenido a la tienda)

# datos del cliente

cliente_vip = True 
articulos_buy = 6 
dias_semana = "Lunes" 

# Regla: descuento mayorista si compra mas de 5 articulos si es VIP 
aplica_mayorista = (articulos_buy > 5 ) and (cliente_vip == True)
print(f"Aplica descuento mayorist? " {aplica_mayorista})

# Regla 2 Descuento especial de lunes si es lunes o es VIP 
descuento =(dia_semana == "Lunes") or (cliente_vip == True)

# Regla 3 Verificar que la tienda no este cerrada 
tienda_cerrada = False 
podemos_vender = not tienda_cerrada
print(f"Podemos vender? {podemos_vender}") 

```


# Ejercicio estudiantes 
Crear un sistema que: 

Pida edad 
pida si tiene membresia premium si/no
Evaluar si puede entrar a la sala exclusiva (mayor de edad 18+) y membresia 

```Python
edad = int(input(""Ingrese su edad))

membresia = input("Cuenta con membresia VIP?")

ingresar = (edad >= 18) and (membresia == "Si")

print(f"Puede ingresar a la sala para mayores de edad?")



```
