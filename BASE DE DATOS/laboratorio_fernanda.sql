-- 1 SELECT 
-- facil
-- SELECT nombre 
-- FROM productos;

-- Intermedio
-- SELECT nombre, precio, stock 
-- FROM productos;

-- Retador
-- SELECT * 
-- FROM productos;


-- 2 DISTINCT
-- facil
-- SELECT DISTINCT categoria 
-- FROM productos;

-- Intermedio
-- SELECT DISTINCT proveedor_id 
-- FROM productos;

-- Retador
-- SELECT DISTINCT precio 
-- FROM productos;



--  3 WHERE 
--  facil
-- SELECT * 
-- FROM productos
-- WHERE categoria = 'Hogar';

--  Intermedio
-- SELECT * 
-- FROM productos
-- WHERE precio = 1200.00;

--  Retador
-- SELECT nombre 
-- FROM productos
-- WHERE categoria = 'Electrónica' AND stock < 10;


--  4 ORDER BY 
--  facil
-- SELECT * 
-- FROM productos
-- ORDER BY nombre;

--  Intermedio
-- SELECT * 
-- FROM productos
-- ORDER BY precio DESC;

--  Retador
-- SELECT * 
-- FROM productos
-- ORDER BY categoria, stock DESC;


--  5 LIKE 
--  facil
-- SELECT * 
-- FROM productos
-- WHERE nombre LIKE 'Monitor%';

--  Intermedio
-- SELECT * 
-- FROM productos
-- WHERE nombre LIKE '%o';

--  Retador
-- SELECT * 
-- FROM productos
-- WHERE nombre LIKE '%Inalámbrico%'
-- ORDER BY precio;


-- 6 AND, OR, NOT 
-- facil
-- SELECT * 
-- FROM productos
-- WHERE categoria = 'Electrónica' AND precio < 100;

--  Intermedio
-- SELECT * 
-- FROM productos
-- WHERE categoria = 'Hogar' OR categoria = 'Mobiliario';

--  Retador
-- SELECT * 
-- FROM productos
-- WHERE categoria <> 'Electrónica' AND stock > 0
-- ORDER BY categoria;


--  7 LIMIT 
--  facil
-- SELECT * 
-- FROM productos
-- LIMIT 2;

--  Intermedio
-- SELECT * 
-- FROM productos
-- ORDER BY precio DESC
-- LIMIT 5;

--  Retador
-- SELECT nombre 
-- FROM productos
-- ORDER BY stock ASC
-- LIMIT 1;


--  8 NULL 
--  facil
-- SELECT * 
-- FROM productos
-- WHERE proveedor_id IS NULL;

--  Intermedio
-- SELECT * 
-- FROM productos
-- WHERE stock IS NULL;

--  10 Retador
-- SELECT * 
-- FROM productos
-- WHERE proveedor_id IS NOT NULL
-- AND stock IS NULL;


--  9 MIN-MAX 
--  facil
-- SELECT MIN(precio) 
-- FROM productos;

--  Intermedio
-- SELECT MAX(precio) 
-- FROM productos
-- WHERE categoria = 'Mobiliario';

--  Retador
-- SELECT MAX(stock) 
-- FROM productos
-- WHERE precio < 500;


--  10 COUNT
--  facil
-- SELECT COUNT(*) 
-- FROM productos;

--  Intermedio
-- SELECT COUNT(*) 
-- FROM productos
-- WHERE proveedor_id IS NOT NULL;

--  Retador
-- SELECT COUNT(*) 
-- FROM productos
-- WHERE categoria = 'Electrónica' AND precio > 100;


--  11 SUM 
--  facil
-- SELECT SUM(stock) 
-- FROM productos;

--  Intermedio
-- SELECT SUM(precio) 
-- FROM productos
-- WHERE categoria = 'Mobiliario';

--  Retador
-- SELECT SUM(precio * stock) FROM productos;


--  12 AVG 
--  facil
-- SELECT AVG(precio) 
-- FROM productos;

--  Intermedio
-- SELECT AVG(stock) 
-- FROM productos
-- WHERE categoria = 'Electrónica';

--  Retador
-- SELECT AVG(precio) 
-- FROM productos
-- WHERE YEAR(fecha_ingreso) = 2024;


--  13 IN 
--  facil
-- SELECT * 
-- FROM productos
-- WHERE id IN (1, 3, 5);

--  Intermedio
-- SELECT * 
-- FROM productos
-- WHERE categoria IN ('Hogar', 'Electrónica');

--  Retador
-- SELECT * 
-- FROM productos
-- WHERE proveedor_id IN (1, 2)
-- ORDER BY nombre;


--  14 BETWEEM
--  facil
-- SELECT * 
-- FROM productos
-- WHERE precio BETWEEN 50 AND 300;

--  Intermedio
-- SELECT * 
-- FROM productos
-- WHERE fecha_ingreso BETWEEN '2024-01-01' AND '2024-03-31';

--  Retador
-- SELECT * 
-- FROM productos
-- WHERE stock BETWEEN 5 AND 20
-- AND categoria = 'Mobiliario';


--  15 ALIAS 
--  facil
-- SELECT nombre AS Articulo 
-- FROM productos;

--  Intermedio
-- SELECT precio AS Costo_Unitario
-- FROM productos
-- ORDER BY Costo_Unitario;

--  Retador
-- SELECT nombre,
--  precio * 0.13 AS Impuesto_Ventas
-- FROM productos;


-- 16 CONCAT
-- facil
-- SELECT CONCAT(nombre, ' - ', categoria)
-- FROM productos;

--  Intermedio
-- SELECT CONCAT('El producto ', nombre, ' cuesta Q', precio)
-- FROM productos;

--  Retador
-- SELECT CONCAT(id, '-', LEFT(categoria, 3)) AS codigo_inventario
-- FROM productos;


-- 17 GROUP BYE
-- facil
-- SELECT categoria
-- FROM productos
-- GROUP BY categoria;

-- Intermedio
-- SELECT categoria, COUNT(*) AS cantidad
-- FROM productos
-- GROUP BY categoria;

--  Retador
-- SELECT proveedor_id,
--  MAX(precio) AS Precio_Max,
--  MIN(precio) AS Precio_Min
-- FROM productos
-- GROUP BY proveedor_id
-- ORDER BY Precio_Max DESC;

-- 18 HAVIND 
-- facil
-- SELECT categoria, COUNT(*) AS total
-- FROM productos
-- GROUP BY categoria
-- HAVING COUNT(*) > 2;

-- Intermedio
-- SELECT categoria, AVG(precio) AS promedio
-- FROM productos
-- GROUP BY categoria
-- HAVING AVG(precio) > 200;

--  Retador
-- SELECT proveedor_id,
--   SUM(precio * stock) AS valor_total
-- FROM productos
-- WHERE stock > 0
-- GROUP BY proveedor_id
-- HAVING valor_total > 500;