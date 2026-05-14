const express = require('express');
const path = require('path');
const app = express();
const port = 3000; 

app.use(express.estatic(path.join(__dirname, 'public')));

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, 'public'));
}); 

app.listen(PORT, () => {
console.log('Servidor escuchando en http://localhost: ${PORT}');
});
