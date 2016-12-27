'''
Python Implementation of a segment tree

Overview
A segment tree solves the problem of finding out some information
about a sublist of list. For example, we'd use a segment tree
to find out the max or min of a range of numbers

Runtime and Space Complexity

Description of tree
A node at index i has 2 children at index 2*i+1 and 2*i+2
The leaf nodes of the tree represent a range of unit length
There is 1 leaf node per element in an array


'''


class SegmentNode(Object):
	def __init__(self, val):
		self.val = val
		

class SegmentTree(Object):
	def __init__(self, nums):
		pass




	# recursively construct the segment tree
	def build_tree(self):


