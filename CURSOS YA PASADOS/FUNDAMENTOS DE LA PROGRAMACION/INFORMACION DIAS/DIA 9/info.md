# ESTRUCTURA DE DATOS 
## DICCIONARIOS 
Se usa lo que se llama "clave y Valor" le ponemos una etiqueta y guardamos dentro de esa el valor 

le ponemos una etiqueta con nombre (clave) a la acaja, y dentro guardamos la info (valor)


```python
clave : valor

```
# sintaxis 
a diferencia de las lists que usan corchetes, los diccionarios crean usando llaves {}. separamos la clave y el valor con dos puntos ":"

```python
producto = {
    "nombre": "Arroz", 
    "precio": 1200,
    "cantidad": 5
}

```

un diccionario es ideal cuando queremos que cada dato tenga una etiqueta clara 

# Acceder a valores 
Para acceder a un valor dentro de un diccionarion usamos: 

diccionario["clave"]

la clave 


## modificar los valores en un diccionario 
<!-- en una lista -->
lista_edades[5] = 50

<!-- en un diccionario -->
producto["precio"] = 1500

<!-- actualizar el precio   -->
producto["cantidad"] = producto["cantidad"] - 1
print(producto)




# EJERCICIO 
crear un diccionario llamado `cliente` con

nombre 
edad
ciudad

imprimir cada valor utilizando la sintaxis correcta. 
Modificar el diccionario `cliente`

- cambiar la ciudad 
- aumentar la edad en 1 

imprimir cada valor utilizando la sintazis correcta 


## agregar un elemento al diccionario 

```python
producto["categoria"] = "Granos"
```

# RECORRER UN DICCIONARIO 
## forma 1 - SOLO LAS CLAVES -

```python
for clave in producto: 
    print(f"clave: {clave}: valor: {producto[clave]}")
    
 ```

     
# comparacion lista vs diccionario 

lista:
    
    
# el diccionario es mas claro y legible 
## errorer comunes
* escrinir mal la clave
* acceder a clave inexistente 
* confundir lista con diccionario 
* olvidar que las claves distinguen mayusculas 



# EJERCICIO 
crear una lista llamada producto donde cada elemento sea un diccionario 
los productos van a tener, nombre, precio, cantidad 
despues de ingresar fin, vamos a mostrar el inventario con: 

nombre          precio          cantidad 


 a una lista siempre le agrego elemenos con apend, 