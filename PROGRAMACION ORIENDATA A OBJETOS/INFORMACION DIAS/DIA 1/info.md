# PARADIGMA 
Objeto 
dentro de la caja fuerte le llamamos producto 

# PROGRAMACION ESTRUCTURADA

# PROGRAMACION ORIENTADA A OBJETOS - POO 
## convenciones de nombre 
### Regla 1 de CamelCase ESCLUSIVO para  clases 
`class`
- no se permiten espacios (prohibido usar guiones bajos)
(UNICA Y EXCLUSIVAMENTE PARA BAUTIZAR CLASES)

**EJEMPLOS CORRECTOS** `Cliente`  `ClienteFrecuente`  `VehiculoDeReparto`  `FacturaMensual`

### Regla 2: snake_case para funciones y variables 
si los nombres estan compuesto por varias palabras lo unimos con un guion bajo 
funciones, listas, diccionarios, variables 

**EJEMPLOS CORRECTOS** `calcular_pago()`, `cliente_frecuente`

## OBJETOS-NOMENCLATURA 
de una clase, creamos otra clase 
poliformismo 
clase: es el molde, es la forma en la que le enseñamos un nuevo concepto. Es un plano arquitectonico, 

instancia el objeto: es la manifestacion fisica y real de nuestro plano. 

## pass - este plano/clase esta es contruccion, es ignorar y darle algo para que no me de error en el codigo

## EJEMPLO DE CONVENCIONES 
```python
# paso 1, definir la clase 
# tenemos que usar la palabra reservada, `class` 
# al final del nombre de la clase, se debe de colocar ":"

class ClienteFrecuente: 
    pass 

# paso 3, creamos una variable y una funcion 
nombre_cliente = "Juan Perez"

def registrar_clienteU(): 
    print("El cliente ha sido guardado")
```

# Fabricando objetos (instalacoion)
proceso de creacion 

```python
class ClienteFrecuente: 
    pass 

cliente1 = ClienteFrecuente()

cliente2 = ClienteFrecuente()

print(ClienteFrecuente)
print(cliente1)
print(cliente2)

```

# Ejercicio practica 
vamos a remodelar la tienda completa, el gerente necesita que la computadora tenga 
cajero 
inventario 
y un vehiculo reparto 
crear un plano utilizand la palabra pass 
ademas fabricar dos objetos reales a partir de la clase "Cajero2. imprimelos en pantalla 

# ejercicio practico 2 
vamos a comprovar que la compu si obedese el nuevo paradigma. Vamos a creer facturas a partir de un mismo molde y le pediremos a Pyhton que nos demuestre, con pruebas fisicas de la memoria, que cada factura es un documento unico e irrepetible. 

# type nos funciona para determinar cual fue la clase base para instanciar el objeto 
cual seria el origen del objeto 
