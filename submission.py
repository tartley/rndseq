import random as rd

class RandomSequence(object):

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


def main():
    seq1 = RandomSequence([111, 222], [0.2, 0.8])
    seq2 = RandomSequence([3, 4], [0.2, 0.8])
    print seq1.next()
    print seq1.next()
    print seq1.next()
    print seq1.next()
    print seq1.next()
    print seq1.next()
    
if __name__ == '__main__':
    main()

