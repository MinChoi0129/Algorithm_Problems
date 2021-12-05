const express = require('express')
const app = express()
const port = 5000
const { User } = require('./models/User')
const bodyParser = require('body-parser')
const mongoose = require('mongoose')

mongoose.connect("mongodb+srv://wjdchs0129:wjdchs012@boiler-plate.fkpxd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
.then(() => console.log('Well connected...'))
.catch(err => console.log(err))

app.use(bodyParser.urlencoded({ extended: true }))
app.use(bodyParser.json())
app.get('/', (req, res) => res.send("민재 공부 테스트!!!"))

app.post('/register', (req, res) => {
    const user = new User(req.body)
    user.save((err, doc) => {
        if (err) return res.json({success: false, err})
        return res.status(200).json({
            success: true
        })
    })
})
app.listen(port, () => console.log(`Example app listening on port ${port}!`))