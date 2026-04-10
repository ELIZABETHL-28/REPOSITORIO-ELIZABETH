# El estilo profesional de python (`@property`)

`cliente.pin = 1234`
property se le llama usar Decoradores

# sintaxis del decorador 
* ***PARA EL GETTERS***: escribimos @property justo encima del metodo. el metodo DEBE y TIENE que llamarse exactamente igual que el atributo privado (sin los guiones bajos) 
* ***PARA EL SETTER***: Escribimos @nombre_del_metodo.setter justo encima del metodo modificador 


## ejercicio 

```python
class Empleado(): 
    def __init__(self):
        self.__salario = 300
        
    @property 
    def salario(self): 
        return self.__salario
    
    @salario.setter
    def salario(self, salario_nuevo):
        if salario_nuevo < 300: 
            print ("ERROR. EL SALARIO DEBE DE SER MAYOR")
        else: 
            self.__salario = salario_nuevo
    
usuario = Empleado()

print(usuario.salario)
usuario.salario = 500
print(f"SALARIO MODIFICADO: ", usuario.salario)
            
```
## ejercicio 2
```python
```

# ATRIBUTOS Y METODOS DE CLASE 
## atributo de clase 
```python
# EJEMPLO 2 ATRIBUTOS Y METODOS DE CLASE 
# ATRIBUTO DE CLASE
class Tienda(): 
    #atributo de la clase (APLICA A TODOS)
    impuesto_iva = 0.13
    
    def __init__(self, productos):
        self.productos = productos
        
print(Tienda.impuesto_iva) # 0.13

# METODO DE LA CLASE
`@classmethod` -> `cls`
self -> objeto 
cls -> clas 
se usa exclusivamente para leer o modificar los atributos de Clase 

```

# RETO INTEGRADOR 
actuar como arquitecto de un software. debes programar el nucleo logico de un Banco 

* INSTRUCCIONES 

1 - crear la clase CuentaBancaria 
2 - Atributos compartidos 
    - el banco maneja una tasa_interes_global que nace en 0.5 
    - el banco lleva un registro de total_cuentas_creadas que nace en 0 
3 - constructor 
    - pide un parametro nombre_titular 
    - crear el atributo privado __titular usando el parametro 
    - crea el atributo privado __saldo e inicializalo por defecto en 0.0
    - sumale 1 al atributo de clase total_cuentas_creadas
4 - Seguridad
    - crea un `@property` llamado `saldo` que actue como Getter
    OJO: no hagas el Setter para el saldo, el saldo no se debe poder sobreescribir con un =, solo debe cambiar mediante depositos y retiros 
    - crea un `@property` llamado titular (Getter)
    - crea su respectivo @titular.setter. la validacion debe asegurar que el nombre no este en blanco 
5 metodos de instancia
    - crea un m

