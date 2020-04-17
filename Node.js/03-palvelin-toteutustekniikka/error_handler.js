const errorHandler = (error, req, res, next) => {
    if (error.statusCode === 500) {
        res.status(500).send({
         error: 'Jotakin meni pieleen!'
        })
    } else {
        res.status(error.statusCode).send({ error: error.message });
    }
}  

module.exports = errorHandler;