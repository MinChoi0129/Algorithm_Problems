const { User } = require('../models/User')

let auth = (req, res, next) => {

    // 쿠키를 클라이언트에서 가져옴
    let token = req.cookies.test_cookie
    User.findByToken(token, (err, user) => {
        if (err) throw err

        if (!user) {
            return res.json({ isAuthenticated: false, error: true})
        }

        req.token = token
        req.user = user
        next()
    })
}

module.exports = { auth }