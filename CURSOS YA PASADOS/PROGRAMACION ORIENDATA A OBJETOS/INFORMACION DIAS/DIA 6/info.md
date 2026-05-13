# REPASO 
- clases, un molde para crear los objetos 
- instancia 
- convenciones, Pascal para clases: MiClaseSeLlamaAsi()
- constructores, nos ayuda a inicializar los atributos de la clase
- __init__(self)

# convenciones
## PascalCase: MiNombe, para el nombre de las clases 
## CamenlCase: miNombre 
## SankeCase: mi_nombre, para los metodos, atributos, variables 

# DEFINICION DE CLASE: 
es el plano, molde, plantilla o receta. 

## DEFINICION DE OBJETO: 
instanciacion de la clase 

## atributos y metodo
- ATRIBUTOS: caracteristicas del objeto, que ese pertenece a una clase
son las caracteristicas o varibales internas 
responde a la pregunta: QUE TIENE EL OBJETO? (COLOR, PRECIO, NOMBRE...)

- METODOS: son las funciones o acciones(verbos)
responde a la pregunta: QUE SABE HACER EL OBJETO? (CAMINAR, ENCENDER, CALCULAR)

- CONCEPTO DE SELF: acceder a un parametro 

parametro: valor que recibe una funcion 
atributo: caracteristica que tiene un objeto 

### EJEMPLO 
def saludar (self, nombre, edad): 
    print(f"Hola {nombre}")

## CONSTRUCTOR
sirve para configurar los datos iniciales obligatorios 
se ejecuta automaticamente al momento de instanciar el objeto 


git config --global user.email