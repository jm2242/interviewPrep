from abc import ABCMeta, abstractmethod
import sys
import unittest
# CONSTANTS
MAX_INT = sys.maxint

class SegmentNode(object):
	def __init__(self, val):
		self.val = val


# Abstract class for a SegmentTree
class SegmentTree(object):
	''' A Segment tree for solving problems related to subsets of lists/arrays
	
	Overview
	A segment tree solves the problem of finding out some information
	about a sublist of list. For example, we'd use a segment tree
	to find out the max or min of a range of numbers

	Runtime and Space Complexity

	Description of tree
	A node at index i has 2 children at index 2*i+1 and 2*i+2
	The leaf nodes of the tree represent a range of unit length
	There is 1 leaf node per element in an array

	Attributes:
		nums: list of nums
		tree: implementation of a segment tree with a list

	Tushar Roy (https://www.youtube.com/watch?v=ZBHKZF5w4YU) was used as
	a resource for building the subclass MinElementTree
	'''
	__metaclass__ = ABCMeta


	# wizardry to return the next power of two
	# returns x if x is a power of two
	def next_greater_power_of_2(self, x):  
		return 2**(x-1).bit_length()

	# recursively construct the segment tree
	# Time to consruct O(4n) = O(n)
	def build_tree(self, treeIndex, low, high):

		# base case -> if low==high, then it's a leaf node
		if low == high:
			self.tree[treeIndex] = self.nums[low]
			return

		# split into two branches and prevent overflow for positive integers
		mid = low + (high - low) / 2

		# recursive tree build calls
		self.build_tree(2*treeIndex+1, low, mid) # left child
		self.build_tree(2*treeIndex+2, mid+1, high) # right child

		# merge step
		self.tree[treeIndex] = self.merge(self.tree[2*treeIndex+1], self.tree[2*treeIndex+2])

	# ABSTRACT METHODS

	@abstractmethod
	def range_query(self, lower, upper, qLow, qHigh):
		# method to query the tree 
		pass

	@abstractmethod
	def merge(self, leftChild, rightChild):
		# method to mergee the result of leftChild and rightChild as the 
		# result for the parent
		pass


class MinElementTree(SegmentTree):
	def __init__(self, nums):

		# original numbers
		self.nums = nums

		# initialize a tree to the highest nearest power of two
		self.tree = (2*self.next_greater_power_of_2(len(nums)) - 1) * [MAX_INT]
		"initialize tree of length {0}".format(self.tree)

		# construct the tree
		self.build_tree(0, 0, len(self.nums)-1)

	def merge(self, leftChild, rightChild):
		return min(leftChild, rightChild)

	''' 3 cases to consider
		- total overlap
		- no overlap
		- partial overlap

	takes in a query range qLow and qhigh, lower, upper and pos ranges
	for the tree
	preconditions: qLow >=0, qHigh <=len(numbers) - 1

	returns the minimum value in the interval
	'''
	def range_query(self, qLow, qHigh, pos=0, low=0, high=None):
		if qLow > qHigh:
			raise Exception("qLow cannot be greater than qHigh")
		if high is None:
			high = len(self.nums)-1
		# total overlap scenario
		if qLow <= low and qHigh >= high:
			return self.tree[pos]

		# no overlap:
		if high < qLow or low > qHigh:
			return MAX_INT

		# partial overlap - search both branches
		# split into two branches and prevent overflow for positive integers
		mid = low + (high - low) / 2
		return min( self.range_query(qLow, qHigh, 2*pos+1, low, mid) , 
				self.range_query(qLow, qHigh, 2*pos+2, mid+1, high) )


class SumElementTree(SegmentTree):
	pass



def min_tree_tests():
	nums = [-1,2,4,0]
	min_tree = MinElementTree(nums)
	assert min_tree.range_query(0,0) == -1
	assert min_tree.range_query(2,3) == 0
	assert min_tree.range_query(3,3) == 0
	assert min_tree.range_query(0,3) == -1
	assert min_tree.range_query(1,2) == 2

	nums2 = [-1,2,4,0,5,8,10,-100]
	min_tree2 = MinElementTree(nums2)
	assert min_tree2.range_query(0,7) == -100
	assert min_tree2.range_query(1,1) == 2
	assert min_tree2.range_query(7,7) == -100
	assert min_tree2.range_query(3,4) == 0
	assert min_tree2.range_query(5,6) == 8

def sum_tree_tests():
	nums = [-1,2,4,0]
	#sum_tree = SumElementTree(nums)





def main():
	
	# run some tests for min
	min_tree_tests()

	
	

if __name__ == "__main__":
	main()



