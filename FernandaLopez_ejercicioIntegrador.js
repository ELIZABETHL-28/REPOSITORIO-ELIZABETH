// FERNANDA ELIZABETH 
// LOPEZ
const libros = [
    { id: 1, titulo: "La mecánica del corazón", disponible: true },
    { id: 2, titulo: "El castillo de arena", disponible: false },
    { id: 3, titulo: "La necesidad de amar", disponible: true },
    { id: 4, titulo: "Madrid me mata", disponible: true },
    { id: 5, titulo: "En un metro de bosque", disponible: false }
];

function obtenerLibrosServidor(callback) {
    console.log("CONECTANDO CON SERVIDOR... ");
    setTimeout(() => {
        const error = Math.random() < 0.2;
        if (error) {
            return callback(
                new Error("INCONVENIENTE CON EL SERVIDOR"),
                null
            );
        }
        callback(null, libros);
    }, 2000);
}

function filtrarDisponibles(lista, criterio) {
    let resultado = [];
    lista.forEach(libro => {
        if (criterio(libro)) {
            resultado.push(libro);
        }
    });
    return resultado;
}

obtenerLibrosServidor((error, datos) => {
    if (error) {
        return console.log(error.message);
    }
    console.log("LIBROS RECIBIOS EXITOSAMENTE");
    const disponibles = filtrarDisponibles(
        datos,
        libro => libro.disponible === true
    );
    console.log("LIBROS DISPONIBLES: ");
    disponibles.forEach(libro => {
        console.log("-", libro.titulo);
    });
});