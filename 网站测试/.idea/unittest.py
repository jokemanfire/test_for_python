import unittest

class TestAddition(unittest.TestCase):
    def setUp(self):
        print("setting up the test")

    def tearDown(self):
        print("Tearing down test")

    def test_two(self):
        total = 2+2
        self.assertEqual(4,total)

if __name__ == '__main__':
    unittest.main()