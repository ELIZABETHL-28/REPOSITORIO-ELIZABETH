# MANEJO DE ARCHIVOS 
## METODOS DE APERTURA
`open()`
REQUIEREN DE DOS PARAMETROS OBLIGATORIOS: el nombre del archivo y el Modo en el que queremos abrirlo

# MODOS DE APERTURA: 
1. **modo `w`** (write/escribir)
    - crea un archivo nuevk 
    **advertencia**: si el archivo ya existe, el modo `w` lo destruye por completo y lo sobreescribe desde cero 

2. **modo `a`** (append/ añadir)
    - abre un archivo existente y coloca le cursos al final. 
    - todo lo que escribamos se agregara sin borrar lo anterior 

3. **modo `r`** (read/leer)
    - solo nos permite el progrs

<!-- 
```python
archivo_prueba = open("archivo.txt", "a")

archivo_prueba.write("HOY APRENDI A ESCRIBIR EN MI ARCHIVO")

archivo_prueba.close()
``` -->

## administrador de contexto `whit open`
with open("archivo.txt", "a") as archivo_prueba: 

## el metodo `read()` 
PYTHON tomara todo el contenido del archivo y lo guardara en una sola varibale de tipo cadena de texto (string)

```python
with open ("cuento.txt", "r") as archivo: 
    contenido = archivo.read()
    print("Contenido completo: ")
    print(contenido)

```

## metodo `readline()` (SIRVE CUANDO NECESITAMOS LEER EL ARCHIVO POCO A POCO)

```python
with open ("lista_alumnos.txt", "r") as archivo: 
    primera_linea = archivo.readline()
    segunda_linea = archivo.readline()

    print("Contenido completo: ")
    print(f"delegado de clase: " {primera_linea})

```

## metodo `readlines()`

```python
with open ("inventario.txt", "r") as archivo: 
    lineas = archivo.readlines()

    print("Contenido completo: ")
    print(f"El arhivo tiene {len(lineas)} productos registrado" )
    print(f"el ultimo producto es: {lineas[-1]}")

```













