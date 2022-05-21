import unittest

from help import Help

#Testing if the help call was true or false
class TestRank(unittest.TestCase):

    def test_is_finish(self):
        my_help = Help()
        self.assertEqual(my_help.is_finish(), False, "should be False")
        my_help.show()
        self.assertEqual(my_help.is_finish(), False, "should be False")
        my_help.close_page()
        self.assertEqual(my_help.is_finish(), True, "should be True")


if __name__ == '__main__':
    unittest.main()
