import unittest
from lecture import randomised_function
from unittest.mock import patch

class MyTestCase(unittest.TestCase):

    @patch('random.randint')
    def test_randomised_function(self, mock_randint):
        mock_randint.return_value = 1
        self.assertEqual('software', randomised_function())


    @patch('random.randint')
    def test_randomised_function_2(self, mock_randint):
        mock_randint.return_value = 10
        self.assertEqual('engineering', randomised_function())
