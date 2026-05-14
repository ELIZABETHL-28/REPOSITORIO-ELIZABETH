## funcion normal 
```js
function saludar (nombre) {
    return "Hola" + nombre 
}
```
## funcion flecha
```js
const saludarFlecha = (nombre) => "Hola, " + nombre 

```

# QUE ES UN CALLBACK 
es una funcion que se pasa con argumentos a otra funcion para que esta la ejecute despues de realizar alguna operacion 

```js
function modify(array, callback) {
    array.push(4); 
    callback(); 

}

const myArray = [1, 2, 3]; 
modify(myArray, function(){
    console.log('EL ARRAY HA SIDO MODIFICADO: ', myArray)
}); 
```


## PASAR DATOS AL CALLBACK 

```js
const apellido = ['Garcia', 'Lopez', 'Martinez']; 

modifyAndReport(apellido, (modifiedArray, newLength) => {
    console.log('EL ARRAY HA SIDO MODIFICADO: ', modifiedArray); 
    console.log('LONGITUD: ', newLength); 
})
```

# QUE ES UN forEach? 
```js
es una metodo de los arrays que sirve para recorrer todos sus elementos y ejecutar una funcion callback por cada u no, en orden 

array.forEach((elemento, indice, arreglo) => {

}, thisArgOpcional)
```

```js
function operar(num1, num2, callback) {
    return callback(num1, num2); 
}

const suma = (a, b) => a+b; 
const resta = (a, b) => a-b; 
const mul = (a, b) => a*b; 
const div = (a, b) => a/b; 

console.log("SUMA: ", operar(10, 5, suma));
console.log("resta: ", operar(10, 5, resta));
console.log("mul: ", operar(10, 5, mul));
console.log("div: ", operar(10, 5, div));

function filtrarArreglo(arr, criterio) {
    let resultado = [];

    arr.forEach (elemento => {
    if(criterio(elemento)){
        resultado.push(elemento); 
    }
})
return resultado; 

}

const datos = [1,2,3,4,5,6,7,8,9,10,11,12]; 

const esPar = num => num % 2 === 0; 
const mayorQUE = num => num > 10 ; 
const esImp = num => num % 3 === 0; 

console.log(filtrarArreglo(datos, esPar)); 

```


# ASINCRONIA 
- JS corre en un solo hilo 
- JS usa un **event loop**

## setTimeuot 
```js
console.log("INICIO")
setTimeout( () => {
    console.log("SE MIESTRA DESPUES DE 2 seg")
}, 2000); 
console.log("fin")
```

callback - cb

## ERROR FIRST 


## ejercicio integrador

###
