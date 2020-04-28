const express = require('express');
//const cors = require('cors');
const morgan = require('morgan');
const app = express();
const port = 3000;
const validateQuery = require('./validateQuery');
const errorHandler = require('./error_handler');
const fetch = require("node-fetch");
const parser = require('./parser');

const url = "https://www.ilmatieteenlaitos.fi/observationdata?station=101004 ";

app.use(morgan('dev'));

const makeReq = async url => {
    const res = await fetch(url); 
    const data = await res.json();

    return data;
};

app.get('/weather', validateQuery.validateQuery, async (req,res, next) => {
    
    const oblista = req.query.observation;
    
    try {
        const data = await makeReq(url);
        const observation = parser.parseData(data, oblista);
        res.send(observation);
    } catch (e) {
        console.log(e);
    }
});

app.use(errorHandler);

app.listen(port, () =>
console.log(`Example app listening on
port ${port}!`))