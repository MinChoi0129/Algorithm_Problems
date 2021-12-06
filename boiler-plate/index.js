const express = require('express')
const app = express()
const port = 5000
const { User } = require('./models/User')
const bodyParser = require('body-parser')
const cookieParser = require('cookie-parser')
const mongoose = require('mongoose')
const config = require('./config/key')

mongoose.connect(config.mongoURI)
.then(() => console.log('Well connected...'))
.catch(err => console.log(err))

app.use(bodyParser.urlencoded({ extended: true }))
app.use(bodyParser.json())
app.use(cookieParser())
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

app.post('/login', (req, res) => {
    User.findOne({email: req.body.email}, (err, user) => {
        if (!user) {
            return res.json({
                loginSuccess: false,
                message: "해당 이메일을 가진 사용자가 없습니다."
            }) 
        }

        user.comparePassword(req.body.password, (err, isMatch) => {
            if (!isMatch) return res.json({loginSuccess: false, message: "올바른 비밀번호가 아닙니다."})
            user.generateToken((err, user) => {
                if (err) return res.status(400).send(err)
                
                res.cookie("test_cookie", user.token)
                .status(200)
                .json({loginSuccess: true, userId: user._id})
            })
        })
    })
})
app.listen(port, () => console.log(`Example app listening on port ${port}!`))