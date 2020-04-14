const express = require('express');
const cors = require('cors')
const app = express();
const port = 3000;

app.use(express.urlencoded())
app.use(cors());
app.use('/', express.static('./web-client/public'));
app.use('/hello', express.static('./hello'));
app.use(express.json())


app.get('/api/exercise', (req, res) =>{
    res.statusCode = 200
    res.send(req.query)
});

app.listen(port, () =>
console.log(`Example app listening on
port ${port}!`))

app.post('/api/exercise', function (req, res) {
    res.statusCode = 200
    const params = req.body;
    let response = '<h1>Hello from Express!</h1>' +
    '<h2>POST parameters</h2>'+
    '<p>I received these parameters: </p>'+
    '<ul>';

    for (let i in params) {
        response += '<li> ${i}: ${params[i]}'
    }
     
    response += '</ul>' 
    res.send(response) //yritetty ties kuinka kauan...
    });

app.post('/api/login', (req, res) =>{  
    if (req.body.user || req.body.pwd == "") {
        res.statusCode = 400;
    }     
    else if (req.body.user == "mark" && req.body.pwd == "giraffe") {
        res.statusCode = 200;
        res.send(JSON.stringify(
            {
                user: req.body.user, 
            }
            ))
    } else {
        res.statusCode = 403;
        res.send();
    }
    
    });

app.get('/api', (req, res) => {
    res.json({ msg: 'Hello, World!' })
    });