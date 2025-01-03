import unittest
from main import add, subtract

class TestMain(unittest.TestCase):
    def test_add(self):
        print("Running test_add()...")  # This will print in Jenkins console
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
    
    def test_subtract(self):
        print("Running test_subtract()...")  # This will also print
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 15), -5)

if __name__ == '__main__':
    unittest.main()
