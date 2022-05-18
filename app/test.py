import unittest
from app.models import User, Post, Comment



class UserTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the user class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_user = User('1','Shaban','gatotadria@gmail.com','abcdefg','Python was created by Guido van Rossum, and released in 1991.','I did not know that')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.id,"1")
        self.assertEqual(self.new_user.username,"Shaban")
        self.assertEqual(self.new_user.email,"gatotoadrian.gmail.com")
        self.assertEqual(self.new_user.password,"abcdefg")
        self.assertEqual(self.new_user.posts,"Python was created by Guido van Rossum, and released in 1991.")
        self.assertEqual(self.new_user.comments,"I did not know that")


class PostTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the post class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Post('1','Python Fact','2022-05-17','Python was created by Guido van Rossum, and released in 1991.','1','I did not know that')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_post.id,"1")
        self.assertEqual(self.new_post.title,"Python Fact")
        self.assertEqual(self.new_post.date_posted,"2022-05-17")
        self.assertEqual(self.new_post.content,"Python was created by Guido van Rossum, and released in 1991.")
        self.assertEqual(self.new_post.user_id,"1")
        self.assertEqual(self.new_post.comments,"I did not know that")

class CommentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the user class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = Comment('1','2022-05-17','I did not know that','1','1')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly 
        '''

        self.assertEqual(self.new_comment.id,"1")
        self.assertEqual(self.new_comment.date_posted,"2022-05-17")
        self.assertEqual(self.new_comment.content,"I did not know that")
        self.assertEqual(self.new_comment.user_id,"1")
        self.assertEqual(self.new_comment.post_id,"1")
       
if __name__ == '__main__':
    unittest.main()
