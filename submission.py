import bisect
import random as rd

def cumulative(sequence):
    total = 0
    for value in sequence:
        total += value
        yield total

class RandomSequence(object):

    def __init__(self, _values, _probabilities, random_function = rd.random):
        '''
        Takes an object of two vectors
        First one is a sel of values
        Second is a set of probabilities
        '''
        assert len(_values) == len(_probabilities), \
            "Values and Probabilities are diff lengths"
        assert len(_probabilities) != 0, \
            "Values or Probabilities are empty"
        if sum(_probabilities) != 1.0:
            raise ArithmeticError("Probabilities don't add up to 1")

        self.random_function = random_function
        self._values = _values

        self.sum_p = list(cumulative(_probabilities))


    def next(self):
        '''
        Chooses a weighted random number from the first vector (values)
        Weights are correponding floats in second vector (probabilities).
        '''
        out_value = bisect.bisect_left(self.sum_p, self.random_function())
        return self._values[out_value]

