import unittest
from src.domino import run_domino, reverse_run_domino

class TestDomino(unittest.TestCase):
    def setUp(self):
        self.text = '\|//|||||\||/\|/|'
        self.n = 3

    def test_incorrect_input_text(self):
        text = '///||\\\\M'
        n = self.n
        with self.assertRaises(ValueError):
            run_domino(text, n)

    def test_incorrect_input_number(self):
        text = self.text
        n = 0
        with self.assertRaises(ValueError):
            run_domino(text, n)

    def test_empty_text(self):
        text = ''
        n = self.n
        expected_output = ''
        result = run_domino(text, n)
        self.assertEqual(result, expected_output)

    def test_single_domino(self):
        text = '/'
        n = self.n
        expected_output = '/'
        result = run_domino(text, n)
        self.assertEqual(result, expected_output)

    def test_correct_inputs_one_iteration(self):
        text = self.text
        n = 1
        expected_output = '\|///|||\\\\||/\|//'
        result = run_domino(text, n)
        self.assertEqual(result, expected_output)

    def test_correct_inputs_many_iterations(self):
        text = self.text
        n = 7
        expected_output = '\|////|\\\\\\||/\|//'
        result = run_domino(text, n)
        self.assertEqual(result, expected_output)

class TestDominoReverse(unittest.TestCase):
    def setUp(self):
        self.text = '\|//|||||\||/\|/|'
        self.n = 3

    def test_reverse_incorrect_input_text(self):
        text = '///||\\\\M'
        n = self.n
        with self.assertRaises(ValueError):
            reverse_run_domino(text, n)

    def test_reverse_incorrect_input_number(self):
        text = self.text
        n = 0
        with self.assertRaises(ValueError):
            reverse_run_domino(text, n)

    def test_reverse_empty_text(self):
        text = ''
        n = self.n
        expected_output = ''
        result = reverse_run_domino(text, n)
        self.assertEqual(result, expected_output)

    def test_reverse_single_domino(self):
        text = '/'
        n = self.n
        expected_output = '/'
        result = reverse_run_domino(text, n)
        self.assertEqual(result, expected_output)

    def test_reverse_correct_inputs_one_iteration(self):
        text = self.text
        n = 1
        expected_output ='||/||||||||||||||'
        result = reverse_run_domino(text, n)
        self.assertEqual(result, expected_output)

    def test_reverse_correct_inputs_many_iterations(self):
        text = self.text
        n = 7
        expected_output = '|||||||||||||||||'
        result = reverse_run_domino(text, n)
        self.assertEqual(result, expected_output)

    def test_reverse_correct_inputs_length_two_different_characters(self):
        text = '/\\'
        n = 1
        expected_output = '||'
        result = reverse_run_domino(text, n)
        self.assertEqual(result, expected_output)

    def test_reverse_correct_inputs_length_two_same_characters(self):
        text = '//'
        n = 1
        expected_output = '/|'
        result = reverse_run_domino(text, n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()