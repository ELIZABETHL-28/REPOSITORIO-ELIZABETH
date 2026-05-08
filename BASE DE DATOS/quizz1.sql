-- EJERCICIO 1 ANALISTA DE OPTIMAZACION 
SELECT nombre, proyecto_actual AS Nombre_del_Proyecto
FROM empleados_proyectos 
WHERE departamento = 'IT' AND salario > 3800 AND proyecto_actual IS NOT NULL 
ORDER BY salario DESC; 

-- EJERCICIO 2 EL AUDITOR DE PRODUCTIVIDAD

-- SELECT departamento, AVG(horas_semanales) AS promedio_horas
-- FROM empleados_proyectos 
--GROUP BY departamento
-- HAVING AVG(horas_semanales) > 30; 