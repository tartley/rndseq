import unittest

import submission as sub

class TestSubmission(unittest.TestCase):

    def test_next_num_returns_only_possible_output(self):
        gen = sub.RandomSequence([123], [1])
        self.assertEqual(gen.next(), 123)
        self.assertEqual(gen.next(), 123)
        self.assertEqual(gen.next(), 123)

    def test_RandomGen_raises_on_empty_distribution(self):
        with self.assertRaises(AssertionError):
            sub.RandomSequence([], [])

    def test_RandomGen_raises_on_sum_probabilities_not_one(self):
        with self.assertRaises(ArithmeticError):
            sub.RandomSequence([111, 222, 333], [0.5, 0.5, 0.5])
        with self.assertRaises(ArithmeticError):
            sub.RandomSequence([111, 222, 333], [0.3, 0.3, 0.3])

    def test_RandomGen_raises_on_lists_not_the_same_size(self):
        with self.assertRaises(AssertionError):
            sub.RandomSequence([111, 222, 333], [0.1, 0.9])

    def test_next_num_output_depends_on_tick_position(self):
        gen = sub.RandomSequence([123, 456], [0.1, 0.9], lambda :0.0)
        self.assertEqual(gen.next(), 123)
        self.assertEqual(gen.next(), 123)
        self.assertEqual(gen.next(), 123)
        gen = sub.RandomSequence([123, 456], [0.1, 0.9], lambda :0.08)
        self.assertEqual(gen.next(), 123)
        self.assertEqual(gen.next(), 123)
        self.assertEqual(gen.next(), 123)
        gen = sub.RandomSequence([123, 456], [0.1, 0.9], lambda :0.1)
        self.assertEqual(gen.next(), 123)
        self.assertEqual(gen.next(), 123)
        self.assertEqual(gen.next(), 123)
        gen = sub.RandomSequence([123, 456], [0.1, 0.9], lambda :0.8)
        self.assertEqual(gen.next(), 456)
        self.assertEqual(gen.next(), 456)
        self.assertEqual(gen.next(), 456)
        gen = sub.RandomSequence([123, 456], [0.1, 0.9], lambda :1.0)
        self.assertEqual(gen.next(), 456)
        self.assertEqual(gen.next(), 456)
        self.assertEqual(gen.next(), 456)

