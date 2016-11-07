
class Node:
	def __init__(self, value):
		self.value = value
		self.leftChild = None
		self.rightChild = None




def inOrder(node):

	if node is not None:
		inOrder(node.leftChild)
		print node.value
		inorder(node.rightChild)
		


