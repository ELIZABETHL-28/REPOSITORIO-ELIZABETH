//
const piloto = process.argv[2]; 
const cargaRaw = process.argv[3]; 
const capacidadRaw = process.argv[4]; 

const carga = Number(cargaRaw); 
const capacidad = Number(capacidadRaw); 

if (!piloto || isNaN(carga) || isNaN(capacidad) || capacidad <= 0) {
    console.log("ARGUMENTOS INVALIDOS"); 
    process.exit(1); 
}

const calcularPorcentaje = (cargaAct, capacidadMax) => {
    return(cargaAct/capacidadMax) * 100; 
}; 

const porcentaje = calcularPorcentaje(carga, capacidad); 

const estado = porcentaje >= 90 ? "PELIGRO" : "SEGURO"; 

const reporte = { 
    piloto: piloto, carga: carga, capacidad: capacidad, porcentaje : porcentaje, estado: estado
}; 

console.log(`ANALIZANDO DESPACHO PARA: ${piloto}...`); 
console.log(reporte); 

if (estado === "PELIGRO") {
    console.log("PESO EXCEDIDO! despegue abortado")
}



