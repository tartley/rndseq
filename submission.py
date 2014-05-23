import random as rd


class RandomSequence(object):

	# Takes an object of two vectors
	# First one is a sel of values
	# Second is a set of probabilities
	def __init__(self,_values,_probabilities):
		self._values = _values
		self._probabilities = _probabilities
		pass
	def next(self):
		# chooses a weighted random number from the first vector (values)
		# Weights are correponding floats in second vector (probabilities).
		tick,total,index = rd.random(),0.0,0
		for i in self._probabilities:
			index += 1
			total += i
			if total >= tick:
				break
		return(self._values[index-1])


def main():
	# Number of individual prints for seq1.next():
	repetitions = 10
	# Large sampling number to check for probabilities:
	Large_Rep = 1000000
	# Ocurrences of each value:
	Counter_111 = 0
	Counter_222 = 0

	################################## Sequences ##############################
	###########################################################################
	seq1 = RandomSequence([111,222],[0.1,0.9])
	###########################################################################
	
	print  str(repetitions) +" Individual Repetitions of .next()"
	for i in range(repetitions):
		print (seq1.next())
	print "Large sampling for .next()"
	for i in range(Large_Rep):
		if seq1.next() == 111:
			Counter_111 += 1
		if seq1.next() == 222:
			Counter_222 += 1

	print "111 occurrences: " + str(float(Counter_111)*100/Large_Rep) + "%"
	print "222 occurrences: " + str(float(Counter_222)*100/Large_Rep) + "%"
  
if __name__ == '__main__':
    main()

