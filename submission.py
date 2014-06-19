import bisect
import random as rd

class RandomSequence(object):

    def __init__(self, _values, _probabilities, random_function = rd.random):
        '''
        Takes an object of two vectors
        First one is a sel of values
        Second is a set of probabilities
        '''
        self.random_function = random_function
        self._values = _values
        self._probabilities = _probabilities

        self.sum_p = []
        self.total = 0
        LV = len(self._values)
        LP = len(self._probabilities)

        for i in self._probabilities:
            self.total += i
            self.sum_p.append(self.total)

        if LV == 0 or LP== 0:
            raise AssertionError("Values or/and Probabilities vector/s is/are empty")
        if LV != LP:
            raise AssertionError("Values and Probabilities vectors' length don't match")
        if sum(self._probabilities) != 1.0:
            raise ArithmeticError("Probabilities don't add up to 1")

    def next(self):
        '''
        Chooses a weighted random number from the first vector (values)
        Weights are correponding floats in second vector (probabilities).
        '''
        out_value = bisect.bisect_left(self.sum_p, self.random_function())
        return(self._values[out_value])

