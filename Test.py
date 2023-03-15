import unittest

from Prog1 import addition

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """ Test case to add 2 nos."""
        data=[23,32]
        result=addition(data)
        self.assertEqual(result,55)

if __name__=='__main__':
    unittest.main()
