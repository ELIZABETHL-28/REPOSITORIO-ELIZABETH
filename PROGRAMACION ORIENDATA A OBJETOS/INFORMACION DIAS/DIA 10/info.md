# HERENCIA BASICA 
# PRINCIPIO DRY: (DON'T REPEAT YOURSELF | NO TE REPITAS)

```PYTHON
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    def comer (self):
        print("COMIENDO...")
        
class Gato: 
    def __init__(self, nombre):
        self.nombre = nombre
    def comer (self):
        print("COMIENDO...")
        

```
# SOLUCION USANDO HERENCIA 
```PYTHON
class Perro:
#CREAR PADRE
class Animal: 
    def comer (self):
        print("EL ANIMAL ESTA COMIENDO")

# 2# EL HIJO
class Perro(Animal):
    pass 

# 3# USO
mi_mascota = Perro()
mi_mascota.comer()
```

### agregando habilidades exlusivas al hijo 
```PYTHON
# la superclase (PADRE)
class Vehiculo(): 
    def encender_motor (self):
        print("EL MOTOR SE HA ENCENDIDO")

    def apagar_motor(self):
        print("EL MOTOR SE HA ENCENDIDO")

# SUBCLASE (HIJA 1)
class Auto(Vehiculo):
    def encender_aire(self):
        print("AIRE ACONDICIONADO ENCENDIDO")

class Moto(Vehiculo):
    def hacer_acrobacia(self)
        print("LEVANTANDO LA RUEDA DELANTERA")

carro = Auto()
moto = Moto()

print("ACCIONES DEL AUTO")
carro.enceder_motor()
carro.encender_aire()

print("ACCIONES DE LA MOTO")
moto.encender_motor
moto.hacer_acrobacia 

# SUBCLASE  (HIJO 2)

```
## CONSTRUCTOR DEL HIJO
```PYTHON
class Padre: 
    class Padre():
    def __init__(self, apellido):
        self.apellido = apellido
        
class Hijo(Padre): 
    def __init__(self, nombre): # peligro! eso borra el __init__ del Padre
        self.nombre = nombre
        
chico = Hijo("Carlos")
print(chico.apellido) # ERROR, el hijo nunca recibio el apellido porque su init aplasto al del padre

```
        
## SOLUCION 
super(). significa literalmente Superclase o Padre. Dentro del init del hijo, llamamos a super(). 
Init() y le pasamos los ingrediente que le corresponde al padre

```PYTHON
class Persona: 
    def __init__(self, nombre):
        self.nombre = nombre # SI LO PONEMOS PRIVADO, SE PUEDE ACCEDER DESDE LA CLASE HIJA PERO NO DESDE FUERA DE LA CLASE 
        
class Estudiante(Persona): 
    def __init__(self, nombre_ingresado, nota_ingresada): 
        super().__init__(nombre_ingresado)

        self.nota = nota_ingresada
        
    def mostrar_info(self): 
        print(f"HOLA, MI NOMBRE ES: {self.nombre} y mi nota es: {self.nota}")

estu1 = Estudiante("Fer", 9.5)
estu2.mostrar_info()

print(estu1.__nombre) # se puede acceder pero no es recomdable porque es un atributo privado 

```

## LAS MUCHAS FORMAS (POLIFORMISMO)
**SOLID**: 
**S - Single responsibility (RESPONSABILIDAD UNICA):**
**O - Open/Closed (ABIERTO Y CERRADO)**
**L - Liskov substitution (sustitucion de liskov)**
**I - Interface segregation (segrefacion de interface)** tiene una medida en las funciones (debe de verse en la pantalla si se pasa es porque tenemos que devidirlo)
**D - Dependency inversion (inversion de dependencias)**

## solucion 

HERENCIA Y POLIFORMISMO NO ES LO MISMO
NI POLIFORMISMO A HERENCIA 

## LA REBELION DLE HIJO (SOBRESCRITURA DE METODOS)


## EL PODER DEL POLIMORFISMO 
perros, gatos y vacas y quiere que todos hagan un sonido, escribiria algo asi: 

`if tipo == "perro": ladrar()`
`if tipo == "gato": maullar()`
`if tipo == "vaca": mugir()`


## COMBINANDO LO VIEJO Y LO NUEVO
### 1. Usar `super()` en metodos normales 

## EL GRAN DEBATE: HERENCIA VS POLIMORFISMO 
# HERENCIA 
reutilizar el codigo, no escribir lo mismo varias veces(1, 2, 3, ...)

# POLIMORFISMO 
reutilizar nombres, mecanismo para el programa principal 


### escenario 1: herencia sin polimorfismo 

### escenario 2: polimorfismo sin herencia 


## RESUMEN 

USAMOS herencia cuando notamos que estamos copiando y pegando los mismo atributos (self.nombre, self.precio) en muchas clases diferenctes

usamos polimorfismos cuando notamos que estamos escribiend muchos if / elif 










