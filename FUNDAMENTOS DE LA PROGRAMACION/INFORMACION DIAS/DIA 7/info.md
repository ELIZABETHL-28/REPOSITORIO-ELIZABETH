Laboratorio listas: El Gestor de Invitados
Imagina que estás organizando una fiesta VIP. Necesitas un programa que te ayude a controlar quién está en la lista de invitados.

Instrucciones del Proyecto
La Lista Principal: Crea una lista vacía llamada lista_invitados.

Funciones que debes programar:

agregar_invitado(nombre): Debe recibir un nombre y usar el método .append() para guardarlo.

mostrar_lista(): Debe usar un ciclo for para imprimir todos los nombres que están en la lista actualmente.

buscar_invitado(nombre): Debe verificar si un nombre ya está en la lista.

Si está, devuelve: "El invitado ya está en la lista".

Si no está, devuelve: "Nombre disponible".

eliminar_invitado(nombre): Debe buscar el nombre y usar .remove() para sacarlo de la lista.

Menú de Usuario:

Usa un menú para que el portero del evento pueda:

2. Registrar nuevo invitado.

3. Ver lista completa.

4. Eliminar a alguien (por si se porta mal).

5. Salir.


## ambito global 

```python
nombre_publico = "Diego"

def informacion_privada(nombre): 
    #ambito locas
    nombre_privado = "Juan Jose"
    apellido_privado = "Mayen"

    print(f"mi nombre completo es: " {nombre_privado} {apellido_privado})

    # print(f"mi nombre publico es: {nombre_publico}") se puede acceder a una variable global pero no es buena practica
    print(f"mi nombre publico es; {nombre}")

    nombre = "Carlos" #esto no afecta la variable global, nombre_publico, es una variable local 


nombre_publico = informacion_privada(nombre publico)
nombre_publico = "Carlos"



print(f"(global) Mi nombre publico es:" )
informacion_privada(nombre_publico)

```


# LISTAS DE LISTAS y DICCIONARIOS 
## LISTAS DE LISTAS (matriz)
CICLOS ANIDADOS 
tambien se conoce como:


listas de listas
matrices
estructura bidimensional 
tabla de filas y comlumnas

| producto | precio | cantidad | 
| -------- | ------ | -------- |
| rice     | 1200   | 5        | 

representacion en python 

```python
inventario = [
    ["Arroz", 1200, 5],
    ["Leche", 900, 10],
    ["Pan", 700, 5]
]
```

* Sintaxis: Se abren corchetes generales y dentro se separan por comas otros corchetes mas pequeños 

```python
print("SISTEMA DE BUSQUEDA")

bodega = [
    ["arroz", "frijoles", "lentejas"],
    ["atun", "sardina", "sopa"],
    ["agua", "jugo", "refresco"]
    
]

# en que fila esta ?
# en que columna esta dentro ?
producto_buscado = bodega [1][1]
print("Producto extraido: ", producto_buscado)


# queremos sacar el agua 
print("Bebida seleccionada", bodega[2][0])


# modificar un dato si se acabo un producto y queremos poner otro 
bodega[2][1] = "Te"
print("Fila de bebidas actualizada: ", bodega[2])

```

# recorrer una matriz 
necesitamos un bucle anidado (un for dentro de otro for) el primer bucle se encarga de bajar por los pisos (filas), y el segundo se encarga de caminar de izquierda a derecha revisando los productos de ese piso (coluumnas)

```python
for fila un matriz_principal:
    for elemento in fila: 
```



