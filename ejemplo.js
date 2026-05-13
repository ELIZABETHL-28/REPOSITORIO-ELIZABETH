// function modify(array, callback) {
//     array.push(4); 
//     callback(); 

// }

// const myArray = [1, 2, 3]; 
// modify(myArray, function(){
//     console.log('EL ARRAY HA SIDO MODIFICADO: ', myArray)
// }); 
// =========================================================

// PASAR DATOS AL CALLBACK 

// function modifyAndReport(array, callback) {
//     console.log('MODIFICANDO EL ARRAY'); 
//     array.push("Perez"); 
//     callback(array, array.length); 
// }
// =========================================================

// const apellido = ['Garcia', 'Lopez', 'Martinez']; 

// modifyAndReport(apellido, (modifiedArray, newLength) => {
//     console.log('EL ARRAY HA SIDO MODIFICADO: ', modifiedArray); 
//     console.log('LONGITUD: ', newLength); 
// })

// =========================================================

// forEach

// const numbers[1, 2, 3, 4, 5 ];
// numbers.forEach(number => {
//     console.log('Numero', number); 
// }); 

// const names = [Alice,  bobi, fausto]; 
// =========================================================


// function operar(num1, num2, callback) {
//     return callback(num1, num2); 
// }

// const suma = (a, b) => a+b; 
// const resta = (a, b) => a-b; 
// const mul = (a, b) => a*b; 
// const div = (a, b) => a/b; 

// console.log("SUMA: ", operar(10, 5, suma));
// console.log("resta: ", operar(10, 5, resta));
// console.log("mul: ", operar(10, 5, mul));
// console.log("div: ", operar(10, 5, div));

// function filtrarArreglo(arr, criterio) {
//     let resultado = [];

//     arr.forEach (elemento => {
//     if(criterio(elemento)){
//         resultado.push(elemento); 
//     }
// })
// return resultado; 

// }

// const datos = [1,2,3,4,5,6,7,8,9,10,11,12]; 

// const esPar = num => num % 2 === 0; 
// const mayorQUE = num => num > 10 ; 
// const esImp = num => num % 3 === 0; 

// console.log(filtrarArreglo(datos, esPar)); 
// =========================================================


// console.log("INICIO")
// setTimeout( () => {
//     console.log("SE MIESTRA DESPUES DE 2 seg")
// }, 2000); 
// console.log("fin")

// =========================================================


// function modifyAsync(array, callback) {
//     console.log('INICIANDO MMOFICICACION ASInCRONA...'); 
//     setTimeout(() => {
//         array.push("perez"); 
//         console.log('MODIFICACION ASINCRONA COMPLETADA'); 
//         callback(array, array.length);
//     }, 2000); 
// }

// const apellidos = 

// =========================================================



// EJERCICIO INTEGRADOR 
const libros = [
    { id: 1, titulo: "La mecánica del corazón", disponible: true}, 
    { id: 2, titulo: "El castillo de arena", disponible: false}, 
    { id: 3, titulo: "La necesidad de amar", disponible: true}, 
    { id: 4, titulo: "Madrid me mata", disponible: false}, 
];

function obtenerLibrosServidor(callback){
    console.log("CONECTANDO AL SERVIDOR..."); 

    setTimeout(() => {
        const errorServidor = Math.random() < 0.20; 

        if (errorServidor) {
            callback(new Error("NO RESPONDE EL SERVIDOR"))
        }
    })
}
