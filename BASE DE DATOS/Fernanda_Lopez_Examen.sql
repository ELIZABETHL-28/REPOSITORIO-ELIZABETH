-- FERNANDA ELIZABETH LOPEZ 
-- PARTE 1 EXAMEN 
-- RELACION Y FILTRO DE GRUPOS
SELECT depa.nombre, AVG(emple.salario) AS PROMEDIO_SALARIAL
FROM departamentos depa
INNER JOIN empleados emple ON depa.id = emple.dept_id 
GROUP BY depa.nombre 
HAVING AVG(emple.salario) > 3500; 


-- CLASIFICACION DE SALARIOS 
SELECT nombre, salario 
CASE 
    WHEN salario > 5000 THEN 'Senior'
    WHEN salario BETWEEN 3000 AND 5000 THEN 'SemiSenior'
    ELSE 'Junior'
END AS Rango
FROM empleados; 

-- EMPLEADOS SIN ASIGNACIONES 
SELECT emple.nombre
FROM empleados emple
LEFT JOIN asignaciones asig ON emple.id = asig.empleado_id 
WHERE asig.empleado_id IS NULL; 

-- BONUS POR PRODUCTIVIDAD 
SELECT emple.nombre, 
CASE 
    WHEN SUM(asig.horas_dedicadas) > 50 THEN emple.salario * 0.10
    ELSE 0 
END AS Bono
FROM empleados emple 
LEFT JOIN asignaciones asig ON emple.id = asig.empleado_id
GROUP BY emple.id, emple.nombre, emple.salario; 

-- DEPARTAMENTOS CON MUCHOS EMPLEADOS 
SELECT depa.nombre, COUNT(emple.id) AS CANTIDAD_TOTAL 
FROM departamentos depa 
INNER JOIN empleados emple ON depa.id = emple.dept_id
GROUP BY depa.nombre 
HAVING COUNT(emple.id) > 5; 


-- PARTE 2 EXAMEN 
-- REQUERIMIENTO DE ESTRUCTURA

CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    nombre VARCHAR (80)
); 

CREATE TABLE instructores(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(80),
    apellido VARCHAR(80),
    correo_electronico VARCHAR(100)
); 


CREATE TABLE cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(120),
    precio DECIMAL(10,2., )
    fecha_lanzamiento DATE, 
    categoria_id INT,
    instructor_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id), 
    FOREIGN KEY (instructor_id) REFERENCES instructores(id)
); 

CREATE TABLE estudiantes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(80),
    apellido VARCHAR(80),
    edad INT,
    fecha_registro DATE
);

CREATE TABLE inscripciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estudiantes_id INT,
    curso_id INT, 
    fecha_inscripcion DATE,
    calificacion INT,
    FOREIGN KEY (estudiantes_id) REFERENCES estudiantes(id), 
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
); 


-- REQUERIMIENTO DE DATOS
INSERT INTO categorias (nombre) VALUES 
('Programacion'), 
('Diseño'), 
('Marketing'); 

INSERT INTO instructores (nombre, apellido, correo) VALUES
('Fer', 'Portillo', 'fer@gmail.com'),
('Josue', 'Valey', 'josue@gmail.com'),
('Wilson', 'Muyus', 'Will@gmail.com');

INSERT INTO cursos (titulo, precio, fecha_lanzamiento, categoria_id, instructor_id) VALUES
('Python', 80, '2023-02-01', 1, 2),
('Photoshop', 50, '2023-04-15', 2, 3),
('SQL Basico', 80, '2023-06-20', 1, 1),
('ADOBE Photoshop', 80, '2023-06-20', 2, 3),
('Marketing Digital', 50, '2023-08-28', 3, 3);

INSERT INTO estudiantes (nombre, apellido, edad, fecha_registro) VALUES
('Andrew', 'Portillo', 20, '2023-02-01'), 
('Luis', 'Jimenes', 19, '2023-02-03'), 
('David', 'Rabanales', 25, '2023-02-07'), 
('Arellys', 'Gomez', 20, '2023-02-09'), 
('Joel', 'Garcia', 30, '2023-02-11'), 
('Javier', 'Letran', 28, '2023-02-13'), 
('Isaac', 'Jolon', 31, '2023-02-15'), 
('Mauricio', 'Garcia', 26, '2023-02-17'); 

INSER INTO inscripciones (estudiantes_id, curso_id, fecha_inscripcion, calificacion) VALUES 
(1, 1, '2023-03-01', 90), 
(1, 2, '2023-03-02', 80), 
(2, 1, '2023-03-03', 65), 
(3, 3, '2023-03-04', 60), 
(4, 2, '2023-03-05', 92), 
(5, 5, '2023-03-06', 75), 
(6, 1, '2023-03-07', 82), 
(7, 2, '2023-03-08', 91), 
(8, 3, '2023-03-09', 76), 
(2, 4, '2023-03-13', 62), 
(1, 5, '2023-03-11', 98), 
(8, 1, '2023-03-12', 88); 

-- REQUERIMIENTO DE CONSULTA (LECTURA Y JOINS)

SELECT curs.titulo, categ.nombre AS CATEGORIA, CONCAT(instruc.nombre, ' ', instruc.apellido) AS INSTRUCTOR
FROM cursos curs 
INNER JOIN categorias categ ON curs.categoria_id = categ.id 
INNER JOIN instructores instruc ON curs.instructor_id = instruc.id; 


-- ESTUDIANTES POR CURSOS 
SELECT curs.titulo, estudet.nombre, estudet.apellido
FROM inscripciones inscrip
INNER JOIN cursos curs ON inscrip.curso_id = curs.id
INNER JOIN estudiantes estudet ON inscrip.estudiantes_id = estudet.id 
WHERE curs.titulo = 'NOMBRE - CURSO'; 

-- CONTABILIDAD 
SELECT curs.titulo, curs.precio * COUNT(inscrip.id) AS TOTAL_INGRESOS
FROM cursos curs
LEFT JOIN inscripciones inscrip ON curs.id = inscrip.curso_id
GROUP BY curs.id; 

-- PROMEDIO DE ESTUDIANTES 
SELECT estudet.nombre, estudet.apellido, AVG(inscrip.calificacion) AS PROMEDIO
FROM estudiantes estudet
INNER JOIN inscripciones inscrip ON estudet.id = inscrip.estudiantes_id
GROUP BY estudet.id 
HAVING PROMEDIO > 70;

-- CURSOS SIN ALUMNOS 
SELECT curs.titulo
FROM cursos curs
LEFT JOIN inscripciones inscrip ON curs.id = inscrip.curso_id
WHERE inscrip.id IS NULL;

-- SEGMENTACION POR EDAD 
SELECT edad, COUNT(*) AS CANTIDAD 
FROM estudiantes
GROUP BY edad 
ORDER BY CANTIDAD DESC; 