const validateQuery = (req, res, next) => {
    
    const observations = ['temperature', 'humidity', 'wind'];
    const observationList = req.query.observations;

    if (!observationList) {
        req.query.observation = observations;
    } else {
        observationList.forEach(element => {
            if (!observations.includes(element)) {
                const err = new Error ('Invalid observation ${element}');
                err.status(400);
                next(err);
            }
            
        });
    }
    
    next();
}
module.exports = validateQuery;