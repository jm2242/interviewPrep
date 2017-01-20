import itertools
import numpy as np


def longestSubsequence(string1, string2):

	# set up 2D table
	rows = len(string2) + 1
	cols = len(string1) + 1
	table = np.array([[0 for x in range(cols)] for y in range(rows)])

	for r, c in range_2d(1, rows, cols):

		# case where characters match: 1 + northwest cel
		if string2[r-1] == string1[c-1]:
			table[r][c] = 1 + table[r-1][c-1]

		# no match case: max(westCell, northCell)
		else:
			table[r][c] = max(table[r-1][c], table[r][c-1])
	print table
	return table[-1][-1]

		




def range_2d(start, rows, cols):
	for r in range(start, rows):
		for c in range(start, cols):
			yield r, c



if __name__ == "__main__":
	string1 = "abcdaf"
	string2 = "acbcf"
	print longestSubsequence(string1, string2)