let users = require('../mocks/users')

module.exports = {
  getAll: function (req, res) {
    const { order } = req.query

    const sortedUsers = users.sort((a, b) => {
      if (order === 'desc') {
        return a.id < b.id ? 1 : -1
      }
      if (order === 'asc') {
        return a.id > b.id ? 1 : -1
      }
    })
    res.send(200, sortedUsers)
  },

  getOne: function (req, res) {
    const { id } = req.params
    const user = users.find((user) => user.id === Number(id))

    if (!user) {
      return res.send(404, { message: 'User not found' })
    }

    res.send(200, user)
  },

  create: function (req, res) {
    const { body } = req
    const lastId = users[users.length - 1].id
    const newUser = {
      id: lastId + 1,
      ...body,
    }
    users.push(newUser)
    res.send(201, newUser)
  },

  update: function (req, res) {
    const { id } = req.params
    const { body } = req
    const user = users.find((user) => user.id === Number(id))

    if (!user) {
      return res.send(404, { message: 'User not found' })
    }

    const index = users.indexOf(user)
    users[index] = {
      ...user,
      ...body,
    }
    res.send(200, users[index])
  },

  delete: function (req, res) {
    const { id } = req.params
    const user = users.find((user) => user.id === Number(id))

    if (!user) {
      return res.send(404, { message: 'User not found' })
    }

    const index = users.indexOf(user)
    users.splice(index, 1)
    res.send(204)
  },
}
