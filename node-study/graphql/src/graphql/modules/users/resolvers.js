import User from '../../../models/User';

export default {
  Users: {
    fullName: () => 'Anything',
  },
  Query: {
    users: User.find(),
    user: (_, { id }) => User.findById(id),
  },
  Mutation: {
    createUser: async (_, { input }, { pubsub }) => {
      const user = await User.create(input);
      pubsub.publish('USER_ADDED', { userAdded: user });

      return user;
    },
    updateUser: (_, { id, input }) => User.updateOne(id, input),
    deleteUser: (_, { id }) => User.findOneAndDelete(id),
  },
  Subscription: {
    userAdded: {
      subscribe: (obj, args, { pubsub }) => pubsub.asyncIterator('USER_ADDED'),
    },
  },
};
