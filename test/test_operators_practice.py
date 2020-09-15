import unittest


class OperatorsTest(unittest.TestCase):
    def test_equal_operator(self):
        a = 7
        b = -2
        self.assertFalse(a == b)

    def test_notequal_operator(self):
        a = 5
        b = 4
        self.assertTrue(a != b)

    def test_greaterthan_operator(self):
        a = 3
        b = 5
        self.assertFalse(a > b)

    def test_lessthan_operator(self):
        a = 2
        b = 3
        self.assertTrue(a < b)

    def test_greatorequal_operator(self):
        a = 4
        b = 5
        self.assertFalse(a >= b)

    def test_lessorequal_operator(self):
        a = 6
        b = 6
        self.assertTrue(a <= b)


if __name__ == '__main__':
    unittest.main()
