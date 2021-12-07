const express = require('express')
const app = express()
const port = 5000
const bodyParser = require('body-parser')
const cookieParser = require('cookie-parser')
const mongoose = require('mongoose')
const config = require('./config/key')
const { User } = require('./models/User')

// x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }))

// json
app.use(bodyParser.json())
app.use(cookieParser())

// DB 연결
mongoose.connect(config.mongoURI)
    .then(() => console.log('Connected to MongoDB...'))
    .catch(err => console.log(err))


    
app.get('/', (req, res) => {
    res.send("NodeJS 학습중<br><br>1234test")
})

app.post('/register', (req, res) => {
    // 회원가입 필수정보를 client에서 받고 이들을 DB로 넣어줌
    const user = new User(req.body)
    user.save((err, userInfo) => {
        if (err) return res.json({success: false, err })
        return res.status(200).json({ success: true })
    })
})

app.post('/login', (req, res) => {
    // 요청 이메일이 DB에 있는지 확인
    User.findOne({ email: req.body.email }, (err, user) => {
        if (!user) {
            return res.json({
                loginSuccess: false,
                message: "해당 이메일을 가진 사용자가 없습니다."
            })
        }

        // 해당 이메일이 DB에 있는 경우 -> 비밀번호 확인
        user.comparePassword(req.body.password, (err, isMatch) => {
            if (!isMatch) {
                return res.json({
                    loginSuccess: false, 
                    message: "올바른 비밀번호가 아닙니다."
                })
            }
            
            // 이메일이 존재하며 비밀번호도 일치하는 경우 토큰 생성
            user.generateToken((err, user) => {
                if (err) {
                    return res.status(400).send(err)
                }
                res.cookie("test_cookie", user.token)
                    .status(200)
                    .json({ 
                        loginSuccess: true,
                        userId: user._id
                    })
            })
        })
    })
})

app.listen(port, () => console.log(`App is online on port ${port}!`))