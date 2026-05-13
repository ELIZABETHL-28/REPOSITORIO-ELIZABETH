## VARIABLES 
let (varibales mutables)
const (constantes)
evitemos usar `var` 

```javascript
let edad = 30
edad = 40 //valido, porque let el cual permite cambio 
console.log(edad)

const impuesto = 013
// impuesto = 0.15 ERROR !!!! las const no se cambian 
```

CONVENCION: **camelCase**

- totalPrecio 
- userName 

TIPOS PRIMITIVOS: 
`number`, `string`, `boolean`, `null`, `undefined`, `bigint`, `symbol`, Y ESTRUCTURADOS COMO `object` y `function` 

```js
const curso = "PROGRAMACION AVANZADA"
let inscritos = 15
inscritos = inscritos +1;

const precio = 19.99; //number
const nombre = "Diego" // string 
const activo = true; //boolean 
const nada = null; //null
let indefinido; //undefined

console.log(typeof precio)

```

# OPERADORES ARITMETICOS, COMPARACION Y LOGICOS 
**aritmeticos:** +, -, *, /, %, **
**comparacion** ===, !==, >, >=, <, <=, 
**logicos** && (AND),  ! (NOT)   " "(OR)

```js
const num1 = 10
const num2 = 3
console.log(num1 +num2)

console.log(5 == "5" ) //true 
console.log(5 === "5" ) //false 

```


## CONDICIONALES 
* `if / else if / else`
* `switch (valor) {case ...}`
* operador ternario: `cond ? exprTrue : exprFalse`

usar `if / else if`  para logica general y `switch` para multiplles casos de un mismo valor 

```js
const nota = 83

let letra

if (nota >= 90) {
    leta = "A"
}
else if(nota >=80){
    leta = "B"
}
else if(nota >=70){
    leta = "C"
}
else {
    leta = "D"
}

console.log(letra)

```

__``switch`

```js
const dia = martes
switch(dia){
    case "lunes": 
        console.log("CLASE TEORICA")
        break
    case "martes": 
        console.log("CLASE CON QUIZZ")
        break
    case "viernes":
        console.log("CLASE CON LABOTATORIO")
        break
    default: 
        console.log("DIA LIBRE")

}

```

- `operador ternario`
```js
const edad = 18

const esAdulto = (edad >= 18) ? "SI, ES MAYOR" : "NO< NO ES MAYOR"

console.log(esAdulto)

```

# EJERCICIO 
TEMPERATURA 

# CICLOS 
`for(inicializacion: condicion: actiualizacion {...})`
`while {condicion} {...}`
`do {...} while {condicion}`

- CICLO FOR 
```js
let suma = 0
for(let index = 1; index <= 5; index++) {
    suma += index
}

console.log(suma)

```

- CICLO DO...WHILE: hazlo al menos una vez 

```js
const passCorrecta = "1234"
let passIngresada = ""

do
{
    passIngresada = "1234"
    console.log("Validando contrasena...")
} while (passIngresada !== passCorrecta);

console.log("Acceso concedido")

```

- `for...of` sobre un array
```js
const frutas = ["Manzanas", "Pera", "Uvas"]
for (const fruta of frutas) {
    console.log*=(fruta)
}

```

## SUBRUTINAS (funciones)

- **DECLARACIONES** `funcion nombre(params) {...}`
- **EXPRESION** `const nombre = function{params} {...}`
- **FLECHA** `const nombre = {params} => {...}`, calbacks
- **parametros por defecto** `function f{a = 0} {...}`
- **RETORNO** `return valor;`

```js
//DECLARACIONES TRADICIONALES
function alCuadrado(num) {
    return num * num
}

//funcion flecha
const esPar = (num) => num % 2 === 0 

// funcion como parametros por defecto
function saludar(nombre = "Estudiante") {
    return `hola ${nombre}!`
}

console.log(alCuadrado(5))
```

# EJERCICIOOOO 

```js
//FOTOS EN WHATS DE MAJO
```

## ARREGLOS Y MATRICES 
```js

const array = [1, 2, 3]

const matriz = [
    [1, 2, 3], 
    [9, 8, 7]
]

console.log(matriz[1][2])
```


## JSON JavaScript Object Notation

### REGLASS 

### DIRECCIONARIO EN PYTHON
}}

