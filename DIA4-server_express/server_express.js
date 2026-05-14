const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.post("/usuario", (req, res) => {
    console.log(req.body);
    // res.send("USUARIO RECIBIDO"); SE PUEDE HACER ESTE O EL DE ABAJO
    res.json({ mensaje: "Usuario recibido", datos: req.body });
});

app.post("/registro", (req, res) => {
    const { nombre, email, password } = req.body;
    console.log(`Nombre: ${nombre}, Email: ${email}, Password: ${password}`);
    //res.json({ mensaje: "Registro exitoso", datos: req.body });
    res.send("<h1>REGISTRO EXISTOSO</h1><p>Gracias por registrarte," + nombre + "!</p>")
    //res.send("<p>Gracias por registrarte," + nombre + "!</p>"); NO SE PUEDEN HACER DOS ENVIOS
});

app.listen(port, () => {
    console.log(`Servidor escuchando en http://localhost:${port}`);
});

// =====================================

app.post("/login", (req, res) => {
  const { usuario, password } = req.body; 


  if (usuario === "admin" && password === "1234") {
    return res.json({
      status: "ok",
      mensaje: "Login exitoso"
    });
  } else {
    return res.json({
      status: "error",
      mensaje: "Credenciales inválidas"
    });
  }
});

