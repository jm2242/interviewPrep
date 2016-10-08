from Queue import *
# takes in a string and return the shuffled string with the following invariant:
# no two identical characters will be next to each other, if possible
# if not possible, return None
def shuffleString(input):
	# edge cases 
	if not input:
		return None

	if len(input) == 1:
		return input

	# queue for the problem
	q = PriorityQueue()

	# generate character frequency table for input:

	freq = {}

	for x in input:
		if x in freq:
			freq[x] += 1
		else:
			freq[x] = 1

	# put in queue with the priority as the - frequency
	# default implementation for get() is to get the smallest 
	# of entry[0] where entry=(prior,ele) 
	for c in freq:
		q.put((-freq[c],c))

	shuffled = []

	# put the first character in
	first = q.get()
	shuffled.append(first[1])

	# return it back into the queue, if there is at least 1 left
	if first[0] + 1 < 0:
		q.put((first[0]+1,first[1]))
	# while there are still elements in the queue
	while not q.empty():
		highest = q.get()
		if shuffled[-1] != highest[1]:
			shuffled.append(highest[1])

			# don't insert if there are 0 occurences left
			if highest[0] + 1 < 0:
				q.put((highest[0]+1,highest[1]))

		# the character was already the last inserted
		# get a new one, append it, append the first one, the return both to queue
		else:

			# if the queue is empty, this means
			# the highest occuring character is the last one
			# left, so we can't make a valid shuffled string
			if q.empty():
				return None
			nextHighest = q.get()
			shuffled.append(nextHighest[1])
			shuffled.append(highest[1])

			if highest[0] + 1 < 0:
				q.put((highest[0]+1,highest[1]))

			if nextHighest[0] + 1 < 0:
				q.put((nextHighest[0]+1,nextHighest[1]))
	return ''.join(shuffled)

def main():
	print "Shuffled String: " + shuffleString('bbaccc')






main()


