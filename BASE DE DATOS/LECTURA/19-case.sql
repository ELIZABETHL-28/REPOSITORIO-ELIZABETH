-- OBTENER TODOS LOS DATOS DE LA TABLA USERS Y ESTABLECER CONDICIONES SEGUN EL VALOR DE LA EDAD

SELECT *,
CASE 
    WHEN age < 15 THEN 'menor de edad'
    WHEN age = 18 THEN 'Acaba de cumplir mayoria de edad'
    ELSE 'Mayor de edad'
END AS "Es mayor de edad?"
FROM users; 
