import unittest
import script


class TestGame(unittest.TestCase):
    def test_input(self):
        result = script.guess(5,5)
        self.assertTrue(result)

    def test_input_incorrect(self):
        result = script.guess(5,1)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
