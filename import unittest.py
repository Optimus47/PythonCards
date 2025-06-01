import unittest

def add(a, b):
    return a +  b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
    def test_add_float(self):
        self.assertAlmostEqual(add(2.5, 3.5), 6.0)
    def test_add_string(self):
        with self.assertRaises(TypeError):
            add("2", "3")

if __name__ == "__main__":
    unittest.main()
