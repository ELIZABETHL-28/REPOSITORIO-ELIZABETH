-- relacion 1:1 
un usuario se realaciona con un dni y un dni se relaciones con un usuario 

CREATE TABLE dni(
    dni_id INT AUTO_INCREMENT, 
    dni_number int NOT NULL,
    user_id INT,
    PRIMARY KEY (dni_id), 
    FOREIGN KEY (user_id) REFERENCES users(user_id)

)

-- ACA VA INFORMACION DEL VIDEO 

-- insertar datos 
-- 1:1
INSERT INTO dni(dni_number, user_id) VALUES (12345678, 1); 
INSERT INTO dni(dni_number, user_id) VALUES (11111111, 2); 


-- 1:N 
INSERT INTO companies(name) VALUES ('Google');
INSERT INTO companies(name) VALUES ('Amazon'); 

UPDATE users SET company_id = 1 WHERE user_id = 1; 
UPDATE users SET company_id = 2 WHERE user_id = 2; 
UPDATE users SET company_id = 3 WHERE user_id = 3; 

INSERT INTO lenguajes(name) VALUES ('Pyhton');
INSERT INTO lenguajes(name) VALUES ('Html');
INSERT INTO lenguajes(name) VALUES ('Java');

