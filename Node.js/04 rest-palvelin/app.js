const express = require('express');
const morgan = require('morgan');
const token = require('./tokens');
const app = express();
const port = 3000;
const bodyParser = require("body-parser");
const authorize = require('./authorize');
app.use(express.json())

const db = require('./db');


app.use(morgan('dev'));
app.use(bodyParser.json());


app.get("/api/v1/pois",  (req,res, next) => {

    const pois = db.getPoi();
    res.status(200).json(pois);   
});

app.post("/api/v1/pois", authorize, (req,res, next) => {
    
    const body = req.body;
    const {name, description, city,  coordinates} = req.body;

    if (name && description && city && coordinates) {
        try {
            db.createPoi(body);    
        } catch(e){
            console.log(e);
        }
        res.status(201).json(body);
    } else {
        res.status(400).json({msg: "Invalid input body"});
    }  

});

app.delete("/api/v1/pois/:id", authorize,  (req,res, next) => {

    const input = req.params.id;
    //console.log(input);
    try {
    const id = db.getPoi(input);
    if (id) {
        db.deletePoi(input);
        res.status(204).json({msg: "Deleted"});
    } else {
        res.status(404).json({msg: "No id found"});
    }
    
    } catch(e){
        console.log(e);
    }

});

app.put("/api/v1/pois/:id", authorize,  (req,res, next) => {

    const input = req.params.id;
    const id = db.getPoi(input);
    const body = req.body;
    const {name, description, city,  coordinates} = req.body;
    
    if (id) {

        if (name && description && city && coordinates) {
            try {
            db.setPoi(id,body);    
            } catch(e){
            console.log(e);
        }
            res.status(200).json(body);
        } else {
        res.status(400).json({msg: "Invalid input body"});
        }
    } else {
        if (name && description && city && coordinates) {
            try {
                db.createPoi(body);
            
            } catch(e) {
                console.log(e);
        }
        res.status(201).json(body);
        
    } else { 
        res.status(400).json({msg: "Invalid input body"});
    } 
    
    
    }
});


app.get("/api/v1/pois/:id",  (req,res, next) => {

    const input = req.params.id;
    //console.log(input);
    try {
    const id = db.getPoi(input);
    if (id) {
        console.log(id);
        res.status(200).json(id); 
    } else {
        res.status(404).json({msg: "no id found"});
    }
    
    } catch(e){
        console.log(e);
    }

});

const users = [
    { username: "mark", password: "giraffe"}
];

app.post("/api/v1/auth",  (req,res, next) => {
    
    const body = req.body;
    const {username, password} = req.body;

    if (users.find(user => user.username === username && user.password === password)) {
        const token = tokens.create(username);
        res.send({token:token})
    } else {
        res.status(401).send();

    }
   

});

app.listen(port, () =>
console.log(`Example app listening on
port ${port}!`));