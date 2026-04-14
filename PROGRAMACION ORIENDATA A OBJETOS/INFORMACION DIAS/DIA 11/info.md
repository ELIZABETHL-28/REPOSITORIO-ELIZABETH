# REPASO 
-herencia 
-polimorfismo = capacidad de respodner de diferentes maneras una accion. 
-super 
-proncipio SOLID
-sobreescritura de metodos
-__str__ 

# sobrecarga de operadores 
+
5+5, 10 matematicas
"hola" + "mundo", "Hola Mundo" (concatenando)

billetera1 + billetera2, 
-para enseñar el +, sobreescribimos `__add__(self, otro_objeto)` (sumar)
-para enseñar el -, sobreescribimos `__sub__(self, otro_objeto)` (restar)
-para enseñar el >, sobreescribimos `__gt__(self, otro_objeto)` (greater than )
-para enseñar el <, sobreescribimos `__lt__(self, otro_objeto)` (less than )
-para enseñar el ==, sobreescribimos `__eq__(self, otro_objeto)` (equal | igual )



## LAS TRES FORMAS 
# 1. Usando la Forma 1: Importar el módulo completo
import random
numero = random.randint(1, 10)
print(f"Número aleatorio: {numero}")

# ---

# 2. Usando la Forma 2: Importar una herramienta específica
from random import choice
nombres = ["Ana", "Luis", "Carlos"]
ganador = choice(nombres)
print(f"El ganador es: {ganador}")

# ---

# 3. Usando la Forma 3: Importar con un alias (apodo)
import math as matematicas
resultado = matematicas.ceil(4.2)
print(f"Redondeo hacia arriba de 4.2: {resultado}")



# PROYECTO 
se acostumbra
herencia esten dividas en clases 
todos a diferentes archivos para no afectar la logica de cada uno. 
cada padre e hijo debe tener su propio archivo 


