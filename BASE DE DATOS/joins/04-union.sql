-- union 
-- me elimina los duplicados 

-- obtiene todos los ids de usuarios de la tabla dni y usuarios (exista o no la relacion)
SELECT users.user_id, dni.user_id
FROM users
left join dni on users.user_id = dni.user_id
union
select users.user_id, dni,user_id
from users
right join dni on users.user_id = dni.user_id
