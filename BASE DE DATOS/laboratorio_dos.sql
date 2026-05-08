-- PARTE 1 - DDL 
CREATE DATABASE estacion_aethelgard; 

USE  estacion_aethelgard; 

CREATE TABLE flota(
    id INT PRIMARY KEY, 
    nombre VARCHAR(50), 
    clase VARCHAR(20), 
    energia INT, 
    escudo INT
); 

-- PARTE 2 - POBLACION DE LA FLOTA (DML)
-- insertar
INSERT INTO flota(id, nombre, clase, energia, escudo)
VALUES (1, 'Centinela-X', 'Combate', 100, 100), (2, 'Carguero-01', 'Carga', 80, 100), (3, 'Titan-Alpha', 'Híbrida', 90, 50);

-- PARTE 3 
-- reducir 
UPDATE flota 
SET energia = 25 
WHERE nombre = 'Centinela-X'; -- tira un error se seguridad del Workbench 
-- pero se le puede poner buscandolo por el id = 1; 

-- aumento
UPDATE flota 
SET escudo = 100 
WHERE nombre = 'Titan-Alpha';
-- TIENE EL BLOQUEO y podemos poner igual al anterior WHERE id = 3; 

-- ELiminar
DELETE FROM flota
WHERE nombre = 'Carguero-01';
-- WHERE id = 2; 