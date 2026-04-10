 # LABORATORIO SEGUIR INSTRUCCIONES DEL PROYECTO 
 ## INDIVIDUAL 


# USO DEL BREAK 
## termina el ciclo
EJEMPLO 

```python
#utiliza una condicion de verdadero y falso. ESTE TRUE DIRA SIEMPRE SERA VERDADERO
while True: 
    name = input("INGRESE SU NOMBRE... (sale para terminar)")

    #ESTE MECANISMO NOS SIRVE PARA SALIR DEL MECANISMO!
    if name == "salir":  
        break 

    print("BIENVENIDO, ", name)


print ("PROGRAMA FINALIZADO")

```

# USO DEL CONTINUE 
## ignora cierto aspecto del codigo y continua en el ciclo 
```python

for product in range (6): 
    if product == 3: 
        continue
    print("PRODUCTO ETIQUETADO: ", product)

```
# EJEMPLO INTEGRADOR DE BREAK Y CONTINUE
```
print ("="*15)
print("ESCANER DE PRODUCTO")
print ("="*15)

#EJjemplo de un BREAK buscando un porducto peligroso
for caja in range (1, 11):
    print(f"escaneando caja {caja}")

    if caja == 5:
        print("ALERTA!!! Producto peligroso encontrado, deteniendo escaneo")


print ("EL ESCANER HA TERMINADO SU REVISON DE SEGURIDAD")



#ejemplo de un CONTINUE ignorando errores

print ("\n"+"="+15)
print("PROCESO DE PAGOS")
print ("="+15)

for cliente in range (1, 6): 
    print(f"PROCESANDO PAGO DEL CLIENTE {cliente}")

    #simulamos que el cliente 5 tiene un error en su pago
    # fondos insuficientes, tarjeta vencida, etc
    if cliente == 5:
        print("ERROR! pago no procesado, saltando al siguiente cliente")
        continue 

    print("PAGO PROCESADO EXITOSAMENTE")
```

# ESTRUCTURA DE DATOS 
## LISTA 
las listas se crean con corchetes
me permite que un mismo estante existan varios tipos de datos diferentes 

## crear una lista
### forma 1: con elementos
mi_lista = [10, "hola", 3.14 ]


### forma 2: sin elementos 
lista_vacia = []

### forma 3: por porcion de la lista (slicing)
`nombre de la lista` + `[`+ `inicio`+ `:`+`final` +`]` : el final no esta incluido  
mi_lista[1:2]

### forma 4: slincing con saltos 
`nombre de la lista` + `[`+ `inicio`+ `:`+`final` +`]`
print(mi_lista[0:4:2])


## ACCEDER A LOS ELEMENTOS 
PARA QUE SIRVE LOS INDICES, 
#### LAS LISTAS TAMBIEN EMPEZAN DESDE 0
### dos pasos
saludo = mi_lista [1] 
print (saludo)

### un paso
print (mi_lista[1])

## agregar elementos (`append`)
### sintaxis 
# `nombre de la lista` + `.` + `append` + `lo que quiere agregar` + `J`

lista_vacia.append ("Diego")

print (lista_vacia[0])

mi_lista.append("mundo")
print(mi_lista)


# RECORRER UNA LISTA

# forma 1: con un ciclo for
```
for elemento in mi_lista:
    print(elemento)

    if elemento == 3.14: 
        print("encontre el numero pi")
        break
```
# forma 2: usando los indices 
```
len(mi_lista) # devuelve la cantidad de elementos que tiene la lista
for indice in range (len(mi_lista)):
    print(mi_lista(indice))
```


# MODIFICAR UN ELEMENTO

mi_lista [1] = "HOLA"


# ELIMINAR UN ELEMENTO
## eliminar un elemento por el indice con `del`
del mi_lista[1]


## eliminar por valor con `remove()`
`nombre de la lista` + `.` + `remove(` + `valor que quiero eliminar` + `)`
mi_lista.remove(10)


## eliminar el ultimo elemento con `pop`
mi_lista.pop()


# ESTRUCTURA DE TUPLAS 
## la tupla es inmutable (es por indice, por valores) una vez creada no se pude modicar los valores que existen adentro (valores puestos en una vitrina quedan permanentemente ahi)

**Sintaxis** En lugar de corchetes [] (listas), usamos parentesis () (tuplas)


### crear tupla 

```python
producto = ("Arroz", 1200, 5)
```

### Acceder a valores 

```python
print(producto[0])
print(producto[1])
```

### recorrer una tuplas 
for producto un productos: 
print(producto)

# Reto 1: El Menú del Restaurante (Listas)

### Enunciado

1. Crea una lista llamada `menu` que contenga 3 platillos.
2. Imprime el segundo platillo usando su índice.
3. Recorre la lista con un bucle `for` e imprime todos los platillos uno por uno.


# Reto 2: Registro de Producto con Tupla

### Enunciado
  
La tienda desea representar cada producto como una tupla con tres elementos:

(nombre, precio, cantidad)

Realiza lo siguiente:

1. Crea una tupla llamada `producto` con los datos:
   - Nombre: "Arroz"
   - Precio: 1200
   - Cantidad: 5
2. Imprime cada elemento usando su índice.
3. Calcula el valor total del producto (precio × cantidad).
4. Intenta modificar el precio dentro de la tupla y observa qué ocurre.






# # --- lista de 3 platillos ---
# menu = ["FRUTTI DI MARE", "SANTA FE", "FIORENTINA"]
 
# print("- - - - - - - - - - - - - - -")
# print("Segundo platillo:", menu[1])
# print("- - - - - - - - - - - - - - -")

# print("\n== Menú completo:==")
# for platillo in menu:
#     print(platillo)


<!-- # --- creacion de tupla ---

producto = ("Arroz", 1200, 5)

# imprimir usando indices
print("Nombre: ", producto[0])
print("Precio: ", producto[1])
print("Cantidad: ", producto[2])

total = producto[1] * producto[2]
print("VALOR TOTAL DEL PRODUCTO: ", total)

# con esto queremos cambiar el valor del producto
producto[1] = 1250 -->