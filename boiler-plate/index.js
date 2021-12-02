const express = require('express')
const app = express()
const port = 5000

const mongoose = require('mongoose')
mongoose.connect("mongodb+srv://wjdchs0129:wjdchs012@boiler-plate.fkpxd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
.then(() => console.log('Well connected...'))
.catch(err => console.log(err))


app.get('/', (req, res) => res.send("Hello World!"))
app.listen(port, () => console.log(`Example app listening on port ${port}!`))