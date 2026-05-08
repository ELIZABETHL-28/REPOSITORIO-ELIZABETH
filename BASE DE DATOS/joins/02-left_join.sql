-- quiero obtener todos los datos de los usuarios junto a su dni 
-- left join: 
-- devuelve todo los registros de la tabla de la izqu (users)
-- y los registros coincidentes de la tabla de la derecha (dni)
-- si no hya councidencia, se rellena con NULL 

SELECT * 
from users LEFT JOIN dni 
ON users.user_id = dni.user_id 


SELECT * 
from dni 