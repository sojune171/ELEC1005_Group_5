import unittest

from rank import Rank

#Testing if the Rank received was True or False
class TestRank(unittest.TestCase):

    def test_is_finish(self):
        my_rank = Rank()
        self.assertEqual(my_rank.is_finish(), False, "should be False")
        my_rank.show()
        self.assertEqual(my_rank.is_finish(), False, "should be False")
        my_rank.close_page()
        self.assertEqual(my_rank.is_finish(), True, "should be True")


if __name__ == '__main__':
    unittest.main()
