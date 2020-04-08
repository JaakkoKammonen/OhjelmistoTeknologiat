const express = require('express');
const app = express();
const port = 3000;

app.use('/', express.static('./web-client/public'))



app.get('/api/exercise?name', (req, res) =>{
    res.statusCode = 200
    res.setHeader('Content-Type', 'application/json')
    res.send(JSON.stringify(
        {
            name: req.query.name, 
            occupation: req.query.occupation,
            placeofbirth: req.query.placeofbirth
        }
        ))
});

app.get('/api/exercise?number', (req, res) =>{
    res.statusCode = 200
    res.setHeader('Content-Type', 'application/json')
    res.send(JSON.stringify(
        {
            number1: req.query.number1, 
            number2: req.query.number2,
        }
        ))
});

app.get('/api/exercise', (req, res) =>{
    res.statusCode = 200
    res.send('This is page without parameters!')
});

app.listen(port, () =>
console.log(`Example app listening on
port ${port}!`))

app.post('/users', function (req, res) {
    res.send('Got a POST request')
    })
    