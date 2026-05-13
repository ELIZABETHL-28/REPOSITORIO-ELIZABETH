# REPASO 
formas de importar librerias
usar un alias `as`
sobre carga de operadores
sobre carga de metodos 
reportar herramientas especificas y no toda la libreria `from [nombre libreria] import [nombre de la herramienta]`
importar nuestras propias librerias (cajas)

## EJERCICIO RAPIDO: 
Estas programando el sistemas de combate de juego de StarWars. necestias gestionar la energia de los sables de luz. 

# CONCEPTO ABSTRACTO 
```python
# ejemplo 1
class FiguraGeometrica(): 
    def calcular_area(self):
        print("NO SE COMO CALCULAR EL AREA. NO SOY UNA FIGURA")
        
class Cuadrado(FiguraGeometrica):
    def calcular_area(self):
        print("Area = lado * lado")
        
figura_fantasma = FiguraGeometrica()
figura_fantasma.calcular_area()

```

## CREANDO EL MOLDE FANTASMA (EL MODULO `abc`)
abc = ABSTRACT BASE CLASSES 
debemos marcar al menos uno de sus metodos con el decorador  @abstractmethod
un metodo abstracto es un metodo vacio. no tiene codigo por dentro. usamos la palabra pass

```python
#IMPORTANCION OBLIGATORIA
from abc import ABC, abstractmethod

class Documento(ABC):
    def __init__(self, titulo):
        self.titulo = titulo
        
    @abstractmethod
    def exportar(self): 
        pass #metodo que los hijos deben de cumplir
    
    #metodo opcion si quiere o no tenerlo, los padres abstractor pueden tener metodos normales
    def mostrar_titulo(self): 
        print("DOCUMENTO: ", {self.titulo})
        
try: 
    doc_invalido = Documento ("Mi  archivo")
except: 
    print("-BLOQUEO DE SEGURIDAD-")
```
**el hijo esta obligado a sobreescribir todos los metodos abstractos del padre**

## EJERCICIO

# PROPIEDADES EXACTAS 
## PROPUEDADES ABSTRACTAS 
ponemos  @property seguido de abstracmethod 
**estas obligado a crear un getter para esta propiedad**

```python

from abc import ABC, abstractmethod

class VehiculoComercial(ABC): 
    @property
    @abstractmethod
    def tarifa_km(self): 
        pass 
    
    def calcular_viaje(self, kilometro): 
        total = kilometro * self.tarifa_km
        print("COSTO DEL VIAJE", {total})
        
class Taxi(VehiculoComercial):
    @property
    def tarifa_km(self):
        return 500
    
mi_taxi = Taxi()
mi_taxi.calcular_viaje(10) # 10*500 = 5000

```


# HERENCIA MULTIPLE 

* EL METODO ABSTRACTO NO PUEDE LLEVAR ALGO MAS QUE SOLO PASS, NO DEBE DE TENER IMPLEMENTACION ! 

























```python

```
