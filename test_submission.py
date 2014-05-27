import unittest

import submission as sft

class TestSubmission(unittest.TestCase):

    def test_RandomGen_raises_on_empty_distribution(self):
        with self.assertRaises(AssertionError):
            sft.RandomSequence([], [])

    def test_next_num_returns_only_possible_output(self):
        gen = sft.RandomSequence([123], [1])
        self.assertEqual(gen.next(), 123)
        self.assertEqual(gen.next(), 123)
        self.assertEqual(gen.next(), 123)

    def test_RandomGen_raises_on_sum_probabilities_not_one(self):
        with self.assertRaises(ArithmeticError):
            sft.RandomSequence([111,222,333],[0.5,0.5,0.5])
        with self.assertRaises(ArithmeticError):
            sft.RandomSequence([111,222,333],[0.3,0.3,0.3])

