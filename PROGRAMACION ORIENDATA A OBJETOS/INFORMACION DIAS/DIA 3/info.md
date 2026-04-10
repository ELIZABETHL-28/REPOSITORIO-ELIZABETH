# 25 MARZO 2026
# CONSTRUCTOR 
* EN PYTHON ES METODO MAGICO PORQUE SE EJECUTA AUTOMATICAMENTE EN EL INSTANTE QUE CREAMOS EL OBJETO 
producto1 = Producto() 

## sintaxis 
`def_init_(self)`

init = inicializar 
EL DOBLE GUION BAJO - metodos exclusivos de funcionamientos de python 


# EJEMPLO

```python
class Libro (): 
    #NUESTRO CONSTRUCCTOR EXIGE DOS INGREDIENTE EXTERNOS
    def __init__(self, titulo_ingresado, autor_ingresado):
        #GUARDAMOS LOS INGREDIENTES (ATRIBUTOS) EN EL INTERIOR DEL OBJETO
        self.titulo = titulo_ingresado
        self.autor = autor_ingresado

# la fabricacion 
# vamos a enviar los ingredientes a nuestra clase para crear un objeto 
libro_nuevo = Libro("El principito", "Antoine de Saint-Exupery")
libro_viejo = Libro("Don Quijote", "Miguel Cervantes")

print(f"EL AUTOR REGISTRADO DEL LIBRO: {libro_nuevo.titulo} es {libro_nuevo.autor}")
print(f"EL AUTOR REGISTRADO DEL LIBRO: {libro_viejo.titulo} es {libro_viejo.autor}")

```


# EJERCICIO 
* cajero: 
    * nombre (afuera)
    * id de empleado (afuera)
    * dinero en caja (valor 0)

    * metodo: 
       -  cobrar articulo
            va a recibir un parametro:  precio del articulo
            sumarle precio del articulo al dinero de la caja 

        - mostrar dinero en caja
            imprimir el dinerop que tiene caja 

* crear dos cajeros (inventar datos, nombre y id)

* cobrar 2 articulo en el cajero1 y 1 articulo en el cajero2

* mostrar el dinero que tiene caja del cajero1 
* mostrar el dinero que tiene caja del cajero2


## parametros opcionales en el constructor 
```python
class Cliente(): 
    
    # el pais por defecto sera Guatemala, a menos que nos diga lo contrario
    def __init__(self, nombre, pais = "Guatemala"):
        self.nombre = nombre
        self.pais = pais 
        
# usando constructor normal
cliente1 = Cliente("Fernanda", "Colombia")

cliente1 = Cliente("Mauricio")

# ----------------------------------------------------------------------------------


# class Cliente(): 
    
#     # el pais por defecto sera Guatemala, a menos que nos diga lo contrario
#     def __init__(self, nombre, pais = "Guatemala"):
#         self.nombre = nombre
#         self.pais = pais 
        
# # usando constructor normal
# cliente1 = Cliente("Fernanda", "Colombia")

# cliente2 = Cliente("Mauricio")

# Cliente3 = Cliente("Panama")


```

## EJEMPLO 
## MODIFICANDO ATRIBUTOS A TRAVES DE METODOS 
```python

class Televisor: 
    def __init__(self, marca):
        self.marca = marca
        self.encendido = False # SERA UN ESTADO INICIAL DE APAGADO 
        self.volumen = 10 # ESTADO INICIAL: VOLUMEN 10
        
    def presionar_boton_encendido(self): 
        # si estaba apagado (false), lo prendemos (true)
        if not self.encendido: #ES LO MISMO DE ABAJO LOS DOS DAN TRUE
        # if self.encendido == False: 
            self.encendido = True
            print(F"El televisor {self.marca} se ha encendido")
        # si estaba encendido (true), lo apagamos (false)
        else: 
            self.encendido = False 
            
    def subir_volumen(self): 
        # if self.encendido == True: LOS DOS DAN TRUE, ES LO MISMO
        if  self.encendido: 
            self.volumen += 1 
            print(f"El volumen actural: {self.volumen}")
        else: 
            print("ERROR: no se puede subir el volumen. El televisor esta apagado...")
        
tv1 = Televisor("SAMSUNG")

tv1.subir_volumen()    
tv1.presionar_boton_encendido()

tv1.subir_volumen()    
tv1.subir_volumen()    

tv1.presionar_boton_encendido()        
tv1.presionar_boton_encendido()        
```
