# EJERCICIO DE REPASO 
INVENTARIO TIENDA DE FRUTAS 
tienes una lista donde cada sublista representa un estante. Cada estante tiene cantidades de frutas. 
Debes calcular cuantas frutas totales hay, pero solo que aquellas que tengan mas de 5 estudiantes 
y sean un numero par. 
Lista de estantes con cantidades de productos



# EJERCICIO DOS 
eres el encargado de un tienda de abarrotes. debido a la inflacion, todos los productos que cuesten menos de 50 pesos deben subir un 10%. los productos que ya cuestan 50 o mas se quedan igual. posteriormente, mostrar los precios finales. 

```python

precios_pasillos = [
    [10.0, 55.0, 20.0],
    [45.0, 80.0, 12.0],
    [100.0, 30.0, 48.0]
]
```

## pseudocodigo 
declarar en una varibale el 10 % de incremento 
recorrer la matriz
aplicar la condicion if 
    si el precio es menor a 50
    aplicar el incremento, el cual es multiplicarlo por el 10
    % guardar/ modificar  guardar/modificar el valor en la lista(matriz)

* mostrar la matriz ya modificada


# CON INDICES 


```python

inventario = [
    [10.0, 55.0, 20.0],
    [45.0, 80.0, 12.0],
    [100.0, 30.0, 48.0]
]

for fila in range (len(inventario)):
    for columna in range(len(inventario[fila])): 
        if columna < 5 and comlumna 
        print(inventario[fila][columna])

        

```
