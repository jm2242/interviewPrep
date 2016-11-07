from minimalTree import *

def inOrderValues(node):

	if node is not None:
		leftValues = inOrderValues(node.leftChild)

		currentValue =  [node.value]
		rightValues = inOrderValues(node.rightChild)

		return leftValues + currentValue + rightValues 

	return []

# cases
# goal has right child -> get right child
# goal does not have rich child -> 




if __name__ == "__main__":
	sortedIntegers = [1,2,3,4,5,6,7,8,9]
	minimumTree = constructTree(sortedIntegers)
	values = inOrderValues(minimumTree)
	print values


#        5
#    3       8
#  2   4   7   9
#1       6 