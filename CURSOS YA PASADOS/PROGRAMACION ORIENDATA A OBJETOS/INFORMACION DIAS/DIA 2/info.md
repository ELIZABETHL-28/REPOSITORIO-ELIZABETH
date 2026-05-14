# OBJETOS
## conceptos como la instancia
# paradigma, el uso del ID y el type 
es como la filosofia del trabajo

# atributos y metodos
atributos son los caracteristicas que nosotroso necesitamos que nuestros objetos tenga 
y los metodos

instancia: atributos 

Ejercicio: 
La tienda se esta expandiendo y necesitamos contratar a tres personas. 
Crea una clase 

# metodos 
un metodo es una funcion `def` existe la palabra importante `self` (YO MISMO)
cuando creamos un metodo un funcion dentro de una clase el primer parametro SIEMPRE, OBLIGATORIAMENTE debe de llamarse `self`


# EJERCICIO 
crear una clase, caja registradora 
dentro de nuestra clase, vamos a crear dos metodos: 
    mostrar dinero actual : imprimir el dineor actual
     procesar venta: todas nuestras ventas son de 500. Añadir a nuestro dinero actual, los 500 de ganancia

luego a fabricar una caja registradora 
le asignamos dinero inicial 
ponemos a trabajr nuestra caja registradora 
    muestre el dinero
    procese una venta 
    muestre el dinero 


# LA TARJETA DE PUNTOS VIP 
en nuestra tienda, los cllientes VIP tiene una tarjeta de puntos. 

Crea una clase llamada TarjetaVIP
Dentro de la clase, crea un metodo llamado mostrar_puntos() que imprima: "Sus puntos acumulados son: [puntos del objeto]"
Crear un segundo metodo llamado sumar_puntos() 

Hasta ahora, nuestros metodos hacian tareas fijas (como saludar). Pero en la vida real, los objetos necesitan interactuar con los clientes. vamos a construir una caja registradora interactiva que le pida el precio al cajero usando input (). Sume ese dinero a su propia memoria y luego imprima un reporte. 


# RETO INTEGRADOR 
vas a crear un programa que simule una mascota digital (como un tamagotchi). La mascota tendra un nombre y un nivel de energia inicial. El usuario podra interactuar con ella para alimentarla (sube energia) o hacerla jugar (bajar energia). el programa debe detenerse si la mascosque se queda sin energia o si el usuario decide salir. 

1. Crea una plantilla llamada Mascota.
2. Al nacer, la mascota debe recibir un nombre y fijar su energía en 100 puntos.
3. Acción de alimentar: Crea una función interna que sume 20 puntos de energía cada vez que se use, pero que no permita exceder el máximo de 100.
4. Acción de jugar: Crea una función que reste 30 puntos de energía. Importante: Usa una condición para verificar si tiene suficiente energía antes de jugar; si tiene menos de 30, debe avisar que está muy cansada.
5. Implementa un bucle que se repita mientras la energía sea mayor a 0.
6. Dentro del bucle, pregunta al usuario qué acción desea realizar (1. Alimentar, 2. Jugar, 3. Salir).
7. Según lo que el usuario escriba, llama al método correspondiente de tu mascota