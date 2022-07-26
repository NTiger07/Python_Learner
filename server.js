const http = require('http')
const { readFileSync } = require("fs")

server = http.createServer((req, res) => {
    const data = readFileSync("./data.json")
    res.end(data)
})

server.listen(5000, () => {
    console.log('Server listening on port 5000...')
})