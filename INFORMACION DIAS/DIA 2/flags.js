// function getFlag(name) {
//  si no existe, me devuelve -1, si existe me devuelve el indice 
//     const idx = process.argv.index0f(`--${name}`); 


    
//     if (idx !== -1 && 
//         idx + 1 < process.argv.length && 
//         process.argv[idx +1] &&
//         !process.argv[idx + 1].startsWith("--")) {
//         return process.argv[idx +1]; 

//     }

//     return "Invitado"; 

// }

// const name = getFlag("name"); 
// const times = Number(getFlag("times")) || 1;


//  siempre necesitamos un valor 
// if (isInteger(times) && times > 0)
// console.log(`Hola ${name}, bienvenido a la progra avanzada`)
// process

// ==========================================================================================


function getFlagValue(nombre) {
    // Buscamos el índice del argumento (ej. "--user")
    const index = process.argv.indexOf(nombre);

    // Verificamos que exista y que tenga un valor después
    if (index !== -1 && process.argv[index + 1]) {
        return process.argv[index + 1];
    }

    return "Invitado"; // Valor por defecto
}

// Probando con diferentes nombres
const name = getFlagValue("--name");
const puesto = getFlagValue("--puesto");

console.log(`Hola ${name}, tu puesto es ${puesto}`);
