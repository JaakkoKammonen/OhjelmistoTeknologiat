const express = require('express');
const cors = require('cors')
const app = express();
const path = require('path');
const port = 3000;

app.use(express.urlencoded())
app.use('/', express.static('./web-client/public'))
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
    res.send('Got a POST request') //yritetty ties kuinka kauan...
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
    }
    
    });

app.get('/api', cors(), (req, res, next) => {
    res.json({ msg: 'Hello, World!' })
    });
app.get('/hello', cors(), (req, res, next) => {
    res.sendfile('./hello')
    });