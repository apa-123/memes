import unittest2

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
        self.assertEqual(self.get_first(), )

    def test_get_second(self):
        self.assertEqual(self.get_second(), )

    def test_get_bio(self):
        self.assertEqual(self.get_bio(), )

    def test_get_picture(self):
        self.assertEqual(self.get_picture(), )

    def test_get_age(self):
        self.assertEqual(self.get_age(), )
    
    def test_get_geography(self):
        self.assertEqual(self.get_geography(), )
    
    def test_get_subreddit(self):
        self.assertEqual(self.get_subreddit(), )
 

if __name__ == '__main__':
    unittest2.main()