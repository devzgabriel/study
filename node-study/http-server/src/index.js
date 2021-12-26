const http = require('http')
const { URL } = require('url')
const bodyParser = require('./helpers/bodyParser')
const routes = require('./routes')

const server = http.createServer((req, res) => {
  const { method, url } = req
  const { pathname, searchParams } = new URL(`http://localhost:3000${url}`)

  let pathnameCopy = pathname
  let id = null
  const splittedPathname = pathnameCopy.split('/').filter(Boolean)

  if (splittedPathname.length > 1) {
    pathnameCopy = `/${splittedPathname[0]}/:id`
    id = splittedPathname[1]
  }

  const query = Object.fromEntries(searchParams)

  const route = routes.find(
    (r) => r.url === pathnameCopy && r.method === method
  )

  if (!route) {
    res.statusCode = 404
    res.end(`Can't find ${method} ${pathnameCopy}`)
    return
  }

  req.query = query
  req.params = { id }

  res.send = (statusCode, body) => {
    res.writeHead(statusCode, { 'Content-Type': 'application/json' })
    res.end(JSON.stringify(body))
  }

  if (['POST', 'PUT', 'PATCH'].includes(method)) {
    bodyParser(req, () => route.handler(req, res))
  } else {
    route.handler(req, res)
  }
})

server.listen(3000, () => console.log('Server running on port 3000'))
