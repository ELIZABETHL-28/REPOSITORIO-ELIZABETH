CREATE TABLE person (
    id, 
    name, 
    age, 
    email,
    fecha_nacimiento
)

CREATE TABLE person (
    id int, 
    name varchar(100), 
    age int, 
    email varchar(50),
    fecha_nacimiento date 
)


CREATE TABLE person2 (
    id int NOT NULL, 
    name varchar(100) NOT NULL, 
    age int, 
    email varchar(50),
    fecha_nacimiento date 
)

CREATE TABLE person3 (
    id int NOT NULL, 
    name varchar(100) NOT NULL, 
    age int, 
    email varchar(50),
    fecha_nacimiento date 
    UNIQUE (id)
)

CREATE TABLE person4 (
    id int NOT NULL, 
    name varchar(100) NOT NULL, 
    age int, 
    email varchar(50),
    fecha_nacimiento date 
    UNIQUE (id)
    PRIMARY KEY (id)
)

-- persona 5 - validar datos
CREATE TABLE person5 (
    id int NOT NULL, 
    name varchar(100) NOT NULL, 
    age int, 
    email varchar(50),
    fecha_nacimiento date 
    UNIQUE (id)
    PRIMARY KEY (id)
    CHECK (age >=18)
)

-- datos por defecto
CREATE TABLE person6 (
    id int NOT NULL, 
    name varchar(100) NOT NULL, 
    age int, 
    email varchar(50) DEFAULT 'invitado@gmail.com',
    fecha_nacimiento date 
    UNIQUE (id)
    PRIMARY KEY (id)
    CHECK (age >=18)
)


CREATE TABLE person7 (
    id int NOT NULL AUTO_INCREMENT, 
    name varchar(100) NOT NULL, 
    age int, 
    email varchar(50) DEFAULT 'invitado@gmail.com',
    fecha_nacimiento date,
    UNIQUE (id),
    PRIMARY KEY (id),
    CHECK (age >=18)
)


insert into person7 (name, age, email, fecha_nacimiento) values ('Miguel', 30, 'miguel@gmail.com', 1996-01-01)

insert into persona7 (name) values ("jose")

