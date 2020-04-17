const express = require('express');
//const cors = require('cors');
const morgan = require('morgan');
const app = express();
const port = 3000;
const validateQuery = require('./validateQuery');
const errorHandler = require('./error_handler');
const fetch = require("node-fetch");

app.use(morgan('dev'));

app.use(errorHandler);

app.get('/weather', errorHandler,(req,res, next) => {
    console.log(res.statusCode)
    
    if (req.statusCode===200){
        res.statusCode==500
        next();
    }
    
      else {
        res.status(200).send(req.query)
    }
});



app.listen(port, () =>
console.log(`Example app listening on
port ${port}!`))