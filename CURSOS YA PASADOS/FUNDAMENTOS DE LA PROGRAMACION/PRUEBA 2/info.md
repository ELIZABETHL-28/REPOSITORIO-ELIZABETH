# Titulo principal (nivel uno)

## subtitulo (nivel dos)

### seccion (nivel tres)

#### subseccion (nivel cuatro)


esto es un ejemplo de *Cursiva* y puedo continuar 

este es otro ejemplo de **negrita**

# viñetas: 
## Listas desordenadas
Ingredientes: 
- Huevos
- Harina 
- Azucar 
    Azucar morena 

## Lista ordenada 
Pasos a seguir: 
1. Precalentar 
2. Mezclas 
3. Hornear 

# Enlaces 
[GOOGLE](google.com)

# Imagenes 
![Ejemplo de imagen](billie.png)

# Citas
hola este es un ejemplo 
>holamundo.py

# Bloques de codigo 
## en un linea 
´print("hola mundo)´

## varias lineas 
```python
    print ("hola mundo)
    print ("hola mundo)
    input()
```



# tablas 
| Nombre | apellido |
| ------ | -------- |
| Diego  | Orozco   | 


# LAS BASES DE CODIGO
# Que es programar?

- crear y dar instrucciones de manera claras y ordenadas, para que una computadora ejecute una tarea.  


## algoritmo / pseudocodigo
- Es una secuencia de pasos ordenados y finitos para resolver un problema
- Un algoritmo no es un codigo 
- CARACTERISTICAS: 
  1. Finito = inicio y fin 
  2. Preciso = Facil de manejar 
  3. Definido = tenemos claro que trabajaremos 


  # ACTIVIDAD 
    hacer el pseudocodigo donde un empleado le venda una bolsa de arroz a un cliente que acaba de entrar a una tienda. 

1. Inicio
* Saludar al cliente
* preguntar que producto desea
* escuchar la respuesta del cliente 
* Caminar al pasillo 3, estante 2
* Tomas 1 bolsa de arroz
* Caminar a la caja registradora
* Decir el precio "Son 3 dollares" 
* Recibir el dinero 
* Entregar el arroz y el cambio
* Despedirse 
* Fin 

# entrada y salida !
## salida 
### la funcion `print()`
restricciones de sintaxis: 
* todo en minuscula 
`PRINT` x 
`Print` X 
* todo a decir va en parentesis () y comillas " " / ' ' 

Example: 
`print ("Hola Mundo")`

Example2: 
`print ('Bienvenido a la tienda digital')`

## funcion de entrada
### la funcion `input ()`
sintaxis: 
* todo en minuscula 
* todo a decir va en parentesis ()
* espera una respuesta
* siempre el input me va a devolver el dato en tipo string 
* almacena el dato en un variable 

```python```

# convenciones 
## camel case 
**ejemplo:** miNombreApellido
## snake case 
**ejemplo:** mi_nombre_apellido 
## pascal 
**ejemplo:** MiNombreApellido

* Usar solo UNA en Python, variado no. 

## codigo explicacion de entrada y salida 
## ejercicio 1: 
Al salir de la tienda, queremos que el sistema le haga 2 preguntas al usuario: Su producto favorito y que calificacion le da a la tienda (1 a 10). Guarda amabas respuestas y al fianl imprime un mensaje de despedida. 


#### solcucion 
```python
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
#Ejercicio de entrada y salida

print("==Queremos saber su opinion==")

pregunta_uno = input("Desea describir su producto favorito: ")
pregunta_dos = input("Que calificacion le das la tienda? (1-10): ")

print (f"El producto favorito es: {pregunta_uno}. Y que calificacion del servicio: {pregunta_dos}")
print ("QUE TENGA EXCELENTE DIA!")

```

## caracteres de escape (\ y \t)

*  \n: salto de linea (enter)
* \t: el tab (da un espacio largo)

```
print ("1. leche")
print ("2. cafe")
print ("3. arroz")

print ("1. leche\n2. cafe\n3. arroz")

print ("producto\t Precio")
print ("1. leche\t Q 2.50")
print ("2. cafe\t Q 2.50")
print ("3. arroz\t Q 2.50")

print ("producto\t Precio\n1. leche\t Q 2.50\n2")
```

# variables 
una variable es un **espacio en memorias** con un **nombre** (etiquetas) donde se guarda un valor. 

## crear variables 
`nombreVariable + signoIgual + el valor`
` nombre            =       "Diego"`

## reglas basicas en los nombre de las variables 
- no usar espacios 
- no se puede iniciar con numero 
- deben de ser descriptivos 
- apegar a una convencion 

MALO: 
```python
4x = 522
x = "hola" 
mi nombre = "Elizabeth" 
``` 

edad1 = 50



# EJERCICIO 
Declarar 3 productos (el usuario va a decir cuales productos)
preguntar el precio de cada producto 
preguntar la cantidad disponible del producto 

generar una factura de inventario; encabezado, producto,: nombre | precio:### | cantidad: #

#### ejercicio ya hecho 
```python

#FACTURAR INVENTARIO 
print("======================")
print("FACTURA DEL INVENTARIO")
print("======================")

#productos 
pro1 = input("NOMBRE DEL PRODUCTO: ")
precio1 = input("PRECIO DEL PRODUCTO: ")
cantidad1 = input("CANTIDAD: ")

pro2 = input("NOMBRE DEL PRODUCTO: ")
precio2 = input("PRECIO DEL PRODUCTO: ")
cantidad2 = input("CANTIDAD: ")

pro3 = input("NOMBRE DEL PRODUCTO: ")
precio3 = input("PRECIO DEL PRODUCTO: ")
cantidad3 = input("CANTIDAD: ")

print("\nINVENTARIO")
print(" Producto \t| Precio \t| Cantidad")
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
print (f"{pro1}\t\t| Q.{precio1}\t\t| {cantidad1}")
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
print (f"{pro2}\t\t| Q.{precio2}\t\t| {cantidad2}")
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
print (f"{pro3}\t\t| Q.{precio3}\t\t| {cantidad3}")
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

#### ejemplo de como mostrar el inventario

print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
print(f"PRODUCT: {pro1:10s} | PRECIO: {precio1:5s} | CANTIDAD: {cantidad1}")
print(f"PRODUCTO: {pro2:10s} | PRECIO: {precio2:5s} | CANTIDAD: {cantidad2}")
print(f"PRODUCTO: {pro3:10s} | PRECIO: {precio3:5s} | CANTIDAD: {cantidad3}")
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

```









  










