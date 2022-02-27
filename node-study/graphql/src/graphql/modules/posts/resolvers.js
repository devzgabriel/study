import Post from '../../../models/Post';
import User from '../../../models/User';

export default {
  Post: {
    author: (post) => User.findById(post.author),
  },
  Query: {
    posts: Post.find(),
    post: (_, { id }) => Post.findById(id),
  },
  Mutation: {
    createPost: (_, { input }) => Post.create(input),
    updatePost: (_, { id, input }) => Post.updateOne(id, input),
    deletePost: (_, { id }) => Post.findOneAndDelete(id),
  },
};
