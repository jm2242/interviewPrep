#from treeTraversals import * -> Look up how to do this
# Given a sorted array of unique integer elements, construct a binary tree of minimal height

class Node:
	def __init__(self, value):
		self.value = value
		self.leftChild = None
		self.rightChild = None

def inOrder(node):

	if node is not None:
		inOrder(node.leftChild)
		print node.value
		inOrder(node.rightChild)


def preOrder(node):

	if node is not None:
		print node.value
		preOrder(node.leftChild)
		preOrder(node.rightChild)

		

def constructTree(sortedIntegers):

	if len(sortedIntegers) == 0:
		return None

	middle = len(sortedIntegers) / 2
	value = sortedIntegers[middle]
	leftList = sortedIntegers[:middle]
	rightList = sortedIntegers[middle+1:]
	
	node = Node(value)
	node.leftChild = constructTree(leftList)
	node.rightChild = constructTree(rightList)


	return node



if __name__ == "__main__":

	sortedIntegers = [1,2,3,4,5,6,7,8,9]
	minimumTree = constructTree(sortedIntegers)
	preOrder(minimumTree)
	#print minimumTree.leftChild.leftChild.leftChild.value
	#print minimumTree.leftChild.leftChild.rightChild


	#     5
	#  2       8
	# 1  3   7   9
	#     4 6    

#        5
#    3       8
#  2   4   7   9
#1       6

