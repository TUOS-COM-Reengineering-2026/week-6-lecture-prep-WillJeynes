import unittest
from prep import strange_function

class MyTestCase(unittest.TestCase):
    def test_strange_function_multiple_cases(self):
    
        test_cases = [
            ((1, 1, 0, 3), 1),
            ((1, 1, 3, 0), 2),
            ((0, 1, 1, 0), 3),
            ((1, 3, 0, 0), 4),
            ((1, 0, 0, 3), 5),
            ((3, 0, 3, 3), 6),
        ]

        for inputs, expected in test_cases:
            with self.subTest(inputs=inputs):
                result = strange_function(*inputs)
                self.assertEqual(result, f"behaviour {expected}")