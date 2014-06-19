import bisect
import random as rd

class RandomSequence(object):

    def __init__(self, _values, _probabilities, random_function = rd.random):
        '''
        Takes an object of two vectors
        First one is a sel of values
        Second is a set of probabilities
        '''
        if len(_values) != len(_probabilities):
            raise AssertionError("Values and Probabilities are diff lengths")
        if len(_probabilities) == 0:
            raise AssertionError("Values or Probabilities are empty")
        if sum(_probabilities) != 1.0:
            raise ArithmeticError("Probabilities don't add up to 1")

        self.random_function = random_function
        self._values = _values
        self._probabilities = _probabilities

        self.sum_p = []
        self.total = 0
        for i in self._probabilities:
            self.total += i
            self.sum_p.append(self.total)


    def next(self):
        '''
        Chooses a weighted random number from the first vector (values)
        Weights are correponding floats in second vector (probabilities).
        '''
        out_value = bisect.bisect_left(self.sum_p, self.random_function())
        return(self._values[out_value])

