import random as rd
import bisect
import time


class RandomSequence(object):

    # Takes an object of two vectors
    # First one is a sel of values
    # Second is a set of probabilities
    def __init__(self,_values,_probabilities):
        self._values = _values
        self._probabilities = _probabilities
        self.sum_p,self.total = [],0
        for i in self._probabilities:
            self.total += i
            self.sum_p.append(self.total)
        if len(self._values) == 0 or len(self._probabilities)== 0:
            raise AssertionError("Values or/and Probabilities vector/s is/are empty")
        if sum(self._probabilities) != 1.0:
            raise ArithmeticError("Probabilities don't add up to 1")

    def next(self):
        # chooses a weighted random number from the first vector (values)
        # Weights are correponding floats in second vector (probabilities).
        out_value = bisect.bisect(self.sum_p,rd.random())

        return(self._values[out_value])


