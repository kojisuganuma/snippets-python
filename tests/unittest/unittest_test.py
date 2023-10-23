import unittest


def add(a, b):
    return a + b


class TestAddition(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # This runs once before all tests in the class.
        pass

    @classmethod
    def tearDownClass(cls):
        # This runs once after all tests in the class.
        pass

    def setUp(self):
        # This runs before each test.
        self.a = 10
        self.b = 5

    def tearDown(self):
        # This runs after each test.
        pass

    def test_add_positive_numbers(self):
        self.assertEqual(add(self.a, self.b), 15)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-self.a, -self.b), -15)


if __name__ == "__main__":
    unittest.main()
