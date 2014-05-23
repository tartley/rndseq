class RandomSequence(object):
    import random as rd
    def __init__(self,_values,_probabilities):
        self._values = _values
        self._probabilities = _probabilities
        pass
    def next(self):
        tick,total,index = rd.random(),0.0,0
        for i in self._probabilities:
            index += 1
            total += i
            if total >= tick:
                break
        return(self._values[index-1])

