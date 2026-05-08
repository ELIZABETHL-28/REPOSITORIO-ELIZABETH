--  El Club de los Identificados (Relación 1:1)
SELECT usr.name, usr.lastname, d.dni_number
FROM users usr
INNER JOIN dni d ON usr.idusers = d.user_id
ORDER BY usr.lastname ASC;


-- Directorio Empresarial (Relación 1:N)
SELECT usr.name, compani.name AS empresa
FROM users usr
INNER JOIN companies c ON u.compani_id = compani.compani_id;

-- Análisis de Inclusión Laboral (Relación 1:N con NULLs)
SELECT usr.name, compani.name AS empresa
FROM users usr
LEFT JOIN companies compani ON usr.compani_id = compani.compani_id

-- Inventario de Habilidades (Relación N:M)
SELECT usr.name, lenguaj.name AS lenguaje
FROM users usr
INNER JOIN users_lenguajes usr.leng ON usr.idusers = usr.leng.user_id
INNER JOIN lenguajes lenguaj ON usr.leng.lenguaje_id = lenguaj.lenguaje_id;

-- Reporte de Popularidad de Lenguajes (N:M Avanzado)
SELECT lenguaj.name AS lenguaje, usr.name
FROM lenguajes lenguaj
LEFT JOIN users_lenguajes ul ON lenguaj.lenguaje_id = usr.leng.lenguaje_id
LEFT JOIN users usr ON usr.leng.user_id = usr.idusers

-- El Reporte Maestro (Múltiples Uniones)
SELECT usr.name, usr.lastname, d.dni_number, compani.name AS empresa
FROM users usr
INNER JOIN dni d ON usr.idusers = d.user_id
INNER JOIN companies compani ON usr.company_id = compani.company_id

-- RETO 

SELECT name, precio
FROM productos
WHERE precio > (SELECT AVG(precio) FROM productos)
ORDER BY precio DESC;

