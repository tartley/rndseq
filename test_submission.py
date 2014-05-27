import unittest

from submission import RandomGen


class TestSubmission(unittest.TestClass):

    def test_RandomGen_raises_on_empty_distribution(self):
        with self.assertRaises(AssertionError):
            RandomGen([], [])

    def test_next_num_returns_only_possible_output(self):
        gen = RandomGen([123], [1])
        self.assertEqual(gen.next_num(), 123)
        self.assertEqual(gen.next_num(), 123)
        self.assertEqual(gen.next_num(), 123)

