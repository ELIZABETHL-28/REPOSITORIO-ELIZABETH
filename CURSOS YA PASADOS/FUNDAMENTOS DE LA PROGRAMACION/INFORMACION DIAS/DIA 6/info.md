# DIA 6 SEMANA 3 16-03-26
# FUNCIONES O METODOS 
a tal objeto darle instrucciones como "vaya a hacer eso" 

## PARA USO DE PONER CODIGO ACA 
```python


```

##  sintaxis 
para crear una funcion, se usa la palabra reservada `def` y esto viene de (**define**) en ingles. Le asignamos un nombre y utilizamos las mismas reglas. Abrimos y terminamos con `:`. 

ocupamos la identacion, (agregandole la sangria para separar e indicar que le pertenece a la funcion)

```python

def saludo(): 
    print("HOLA! como estas")

```

# siempre poner las cosas claras, poner siempre primero las definiciones y luego usarlas 

* Declarar e invocar 

`menu ()` es una funcion 
`menu` es una variable 


```python
# aca le enseño que saludar se hace esto... 
def saludo(): 
    print("HOLA! como estas")

def despedida(): 
    print("Adios, que tengas un excelente dia")

def realizar_operacion (a, b): 
    return a + b  

def menu():
    print ("1 saludar")
    print ("2 despedir")
    print ("3 salir")

    opcion = input("Seleccione una opcion: ")

    while True: 
        match opcion: 
         case "1": 
            saludo()
         case "2": 
            despedida()
         case "3": 
            print("Saliendo...")
            break         
         case _:
            print("opcion invalida")

        opcion = input("Seleccione una opcion: ")

menu() # aca ya me tiene que saludar porque le enseñe como hacerlo 
```


# PARAMETROS EN UNA FUNCION 
caracteristicas o valores dentro de los parentesis. Valores que se reciben del usuario para poder realizar operaciones 


```python
# aca le enseño que saludar se hace esto... 
def saludo(nombre): 
    print("HOLAAAAAA!")
    print(f"COMO ESTAS?, {nombre}")

def despedida(nombre): 
    print("Adios, que tengas un excelente dia")
    print(f"Hasta luego! {nombre}")

def realizar_operacion (a, b): 
    return a + b  

def menu():
    print ("1 saludar")
    print ("2 despedir")
    print ("3 salir")

    opcion = input("Seleccione una opcion: ")

    nombre = input("Ingrese su nombre: ")

    while True: 
        match opcion: 
         case "1": 
            saludo(nombre)
         case "2": 
            despedida(nombre)
         case "3": 
            print("Saliendo...")
            break         
         case _:
            print("opcion invalida")

        opcion = input("Seleccione una opcion: ")

menu() # aca ya me tiene que saludar porque le enseñe como hacerlo 
```

# retorno de los valores `return`
devuelve un valor o varios al punto de invocacion   
Termina tu trabajo 

return es que lo que pasa en una funcion ahi mismo va a morir, 
return es como un salto obligatorio, 

desde que encuentre el return primero ah
return print ("Hola Alice, como estas!")
# UN PRINT NO SE PUEDE RETORNAR 


```python
# funcion con vasios puntos de retorno
def generar_mensaje(nombre): 
    if nombre == "Alice": 
        return "Hola Alice, como estas!"

        # esto no se va a ejecutar porque el return anterior ya termino la funcion
        apellido = input("Ingrese su apellido: ")
        return f"Hola {nombre} {apellido}, como estas?"
    
    elif nombre == "Bob": 
        return "Hola Bob, como estas!"

    else nombre == "Alice": 
        return "Hola, como estas!"

```



# ejercicios estudiantes
## 1. función simple ( sin parámetro ni retorno)
Una pequeña tienda desea mostrar un mensaje de bienvenida cada vez que un cliente entra al sistema.
Cree una función llamada `mensaje_bienvenida()` que muestre el siguiente mensaje:
```
Bienvenido al sistema de ventas
Esperamos que tenga una excelente compra
```

## 2. función con parámetros
Un sistema de gimnasio desea saludar a cada cliente por su nombre.

Cree una función llamada `saludar_cliente(nombre)` que reciba el nombre del cliente como parámetro e imprima el siguiente mensaje:
```
Hola Diego, bienvenido al gimnasio
```

## 3. función con retorno 
Un supermercado desea calcular el precio final de una compra.
Cree una función llamada `calcular_total(precio, cantidad)` que:
* Reciba el precio de un producto.
* Reciba la cantidad comprada.
* Calcule el total a pagar.
* Devuelva el resultado al programa principal.

El programa debe mostrar el total final.

## 4. ejercicio integrador
Una sala de videojuegos vende fichas para poder jugar en las máquinas.
Cada ficha cuesta 500 colones.

El sistema debe permitir que varios clientes compren fichas durante el día.
El programa debe:

1. Mostrar un menú con las siguientes opciones:
```
1 - Comprar fichas
2 - Salir
```

2. Si el cliente desea comprar fichas:
* pedir el nombre del cliente
* pedir cuánto dinero tiene
* calcular cuántas fichas puede comprar
* calcular cuánto dinero le sobra

3. Reglas del sistema:
* si el cliente no tiene dinero suficiente para al menos una ficha, el sistema debe indicarlo
* si tiene suficiente dinero, se debe mostrar:
```
Cantidad de fichas que puede comprar
Dinero de vuelto
```

4. El programa debe repetirse usando un ciclo while hasta que el usuario elija salir.
5. El cálculo de fichas debe realizarse mediante una función con parámetros y retorno.


## Retos
### Reto 1: El Verificador de Edades
* **Instrucción:** Crea una función llamada `es_mayor_de_edad` que reciba un parámetro llamado `edad`. 
    * Dentro de la función, evalúa si la edad es mayor o igual a 18.
    * Si lo es, la función debe DEVOLVER (`return`) el valor booleano `True`. De lo contrario, devolver `False`.
    * En el programa principal, pide la edad al usuario, llama a la función, y usa el resultado devuelto en un `if` para imprimir "Puedes comprar alcohol" o "Venta denegada".

### Reto 2: Calculadora de Descuentos
* **Instrucción:** Crea una función llamada `aplicar_descuento` que reciba dos parámetros: `precio` y `porcentaje_descuento`. La función debe calcular cuánto dinero se descuenta, restarlo al precio original y usar `return` para devolver el nuevo precio. Pruébala con un artículo de 5000 colones y un descuento del 20%.
