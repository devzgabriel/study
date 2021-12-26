const UserController = require('./controllers/UserController')

module.exports = [
  {
    url: '/users',
    method: 'GET',
    handler: UserController.getAll,
  },
  {
    url: '/users/:id',
    method: 'GET',
    handler: UserController.getOne,
  },
  {
    url: '/users',
    method: 'POST',
    handler: UserController.create,
  },
  {
    url: '/users/:id',
    method: 'PUT',
    handler: UserController.update,
  },
  {
    url: '/users/:id',
    method: 'DELETE',
    handler: UserController.delete,
  },
]
