from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {
            1: {'n': 3, 'k': 1, 'output': '0'},
            2: {'n': 4, 'k': 11, 'output': '1'}
        }
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        n, k, output = self.__testCases[1].values()
        result = self.__obj.findKthBit(n = n, k = k)
        self.assertIsInstance(result, str)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        n, k, output = self.__testCases[2].values()
        result = self.__obj.findKthBit(n = n, k = k)
        self.assertIsInstance(result, str)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()