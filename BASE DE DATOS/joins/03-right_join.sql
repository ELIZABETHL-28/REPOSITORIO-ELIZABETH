-- obtner todos los dnis junto a su usuario (lo tenga o no)
-- right join: 
-- devuelve todos lso registros de la tabla de la derecha (dni)
-- y los registros coincidentes de la tabla de la izquieda (users)


SELECT * 
from users RIGHT JOIN dni 
ON users.user_id = dni.user_id


SELECT users.name, dni.dni_number
from users RIGHT JOIN dni 
ON users.user_id = dni.user_id

SELECT users.name, dni.dni_number
from dni RIGHT JOIN users
ON users.user_id = dni.user_id

-- OBTENER EL NOMBRE DE TODOS LOS LENGUAJES JUNTO A SUS USUARIOS (LOS TENGA O NO)
