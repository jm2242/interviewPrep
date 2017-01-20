import numpy as np


def knapsack(items, totalWeight):
        """
    :type items: List[(int, int)]
    :type totalWeight: int
    :rtype: int
    """

	''' 
	each element in items is a tuple of (weight, value) representing
	the weight and value of the item
	index 0 -> weight
	index 1 -> value

	Table structure
	each row of table represents each item
	each collumn represents the total weight of the knapsack
	'''

	# sort the items by weight if not already sorted
	items.sort()

	# set up 2D table
	rows = len(items)
	cols = totalWeight + 1
	table = np.array([[0 for x in range(cols)] for y in range(rows)])


	# fill in first row
	smallest = items[0]
	for c in range(cols):
		if c >= smallest[0]:
			table[0][c] = smallest[1]

	# fill in the rest of the rows
	for r in range(1, rows):

		# get the current item
		item = items[r]

		# c represents the weight being examined in this itteration
		for c in range(cols):

			# if item weight is heavier than the sack capacity, store the value 
			# given by the row above at the same column index
			if c < item[0]:
				table[r][c] = table[r-1][c]

			else:
				remaining_weight = c - item[0]
				table[r][c] = max( item[1] + table[r-1][remaining_weight], table[r-1][c] )

	# return the last slot in the table
	print table
	return table[-1][-1]


def main():
	items = [(1,1), (3,4), (4,5), (5,7)]
	print knapsack(items, 7)


if __name__ == "__main__":
	main()





































