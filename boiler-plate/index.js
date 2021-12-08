const express = require('express')
const app = express()
const port = 5000
const bodyParser = require('body-parser')
const cookieParser = require('cookie-parser')
const mongoose = require('mongoose')
const config = require('./config/key')
const { User } = require('./models/User')
const { auth } = require('./middleware/auth')

// x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }))

// json
app.use(bodyParser.json())
app.use(cookieParser())

// DB 연결
mongoose.connect(config.mongoURI)
    .then(() => console.log('MongoDB에 연결되었습니다.'))
    .catch(err => console.log(err))

app.get('/', (req, res) => {
    res.send("NodeJS 학습중<br><br>1234test")
})

app.post('/api/users/register', (req, res) => {
    // 회원가입 필수정보를 client에서 받고 이들을 DB로 넣어줌
    const user = new User(req.body)
    console.log("회원가입 시도\n", user) // 디버깅
    user.save((err, userInfo) => {
        if (err) {
            console.log("오류 발생\n", err)
            return res.json({ success: false, err })
        }
        return res.status(200).json({ success: true })
    })
})

app.post('/api/users/login', (req, res) => {
    // 요청 이메일이 DB에 있는지 확인
    User.findOne({ email: req.body.email }, (err, user) => {
        if (!user) {
            console.log(`이메일 ${req.body.email}을 가진 사용자가 없습니다.`)
            return res.json({
                loginSuccess: false,
                message: "해당 이메일을 가진 사용자가 없습니다."
            })
        }

        // 해당 이메일이 DB에 있는 경우 -> 비밀번호 확인
        user.comparePassword(req.body.password, (err, isMatch) => {
            if (!isMatch) {
                console.log("올바른 비밀번호가 아닙니다.")
                return res.json({
                    loginSuccess: false,
                    message: "올바른 비밀번호가 아닙니다."
                })
            }

            // 이메일이 존재하며 비밀번호도 일치하는 경우 토큰 생성
            user.generateToken((err, user) => {
                if (err) {
                    console.log("토큰 생성 중 오류 발생")
                    return res.status(400).send(err)
                }

                console.log("로그인 성공 후 토큰 생성 후 쿠키에 저장 완료")
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

app.get('/api/users/auth', auth, (req, res) => {
    res.status(200).json({
        _id: req.user._id,
        isAdmin: req.user.role === 0 ? false : true,
        isAuthenticated: true,
        email: req.user.email,
        name: req.user.name,
        lastname: req.user.lastname,
        role: req.user.role,
        image: req.user.image
    })
})

app.get('/api/users/logout', auth, (req, res) => {
    User.findOneAndUpdate(
        { _id: req.user._id },
        { token: "" },
        (err, user) => {
            if (err) {
                console.log("로그아웃 실패")
                return res.json({ success: false, err })
            }
            console.log(`사용자 ${req.user.name}을 로그아웃합니다.`)
            return res.status(200).send({ success: true })
        })
})

app.listen(port, () => console.log(`포트 ${port}를 개방 중!`))