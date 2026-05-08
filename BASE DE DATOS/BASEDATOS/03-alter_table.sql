-- agregarw un elemento (nueva columna)

alter table person8 
add telefono varchar(20); 

alter table person8
add apellido varchar(100) not null;

-- renombrar una columna 
alter table person8
rename colum apellido to lastname; 

-- modificar un tipo de dato de un atributo 
alter table person8
modify COLUMN telefono int; 


-- eliminar un atributo 
alter table person8
drop column telefono; 

