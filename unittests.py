import unittest2
import categoryClass import Category
import userClass import User

#WIP figuring out unit tests

class TestCategoryMethods(unittest.TestCase):

    def test_get_picture(self):
        self.assertEqual(self.get_picture(), )

    def test_get_subreddit(self):
        self.assertEqual(self.get_subreddit(), )

    def test_get_bio(self):
        self.assertEqual(self.get_bio(), )

class TestUserMethods(unittest.TestCase):

    def test_get_first(self):
        self.assertEqual(self.returnFirstName(), )

    def test_get_second(self):
        self.assertEqual(self.returnSecondName(), )

    def test_get_bio(self):
        self.assertEqual(self.returnBio(), )

    def test_get_picture(self):
        self.assertEqual(self.returnAge(), )

    def test_get_age(self):
        self.assertEqual(self.returnGeography(), )
    
    def test_get_geography(self):
        self.assertEqual(self.returnSubreddit, )

if __name__ == '__main__':
    unittest2.main()