import bisect
import random as rd

def RandomSequence(_values,_probabilities,RF = rd.random):

    sum_p,total,LV,LP = [],0,len(_values),len(_probabilities)
    for i in _probabilities:
        total += i
        sum_p.append(total)
    if LV == 0 or LP == 0:
        raise AssertionError("Values or/and Probabilities vector/s is/are empty")
    if LV != LP:
        raise AssertionError("Values and Probabilities vectors' length don't match")
    if sum(_probabilities) != 1.0:
        raise ArithmeticError("Probabilities don't add up to 1")
    while True:
        yield (_values[bisect.bisect_left(sum_p,RF())])

