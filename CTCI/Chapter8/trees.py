__author__ = 'jonathanmares'

class Node:
    def __init__(self,value, left=None,right=None):
        self.value = value
        self.left = left
        self.right = right


def postorder(node):

    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value)


def inorder(node):

    if not node:
        return
    postorder(node.left)
    print(node.value)
    postorder(node.right)


def main():
    c = Node(6)
    b = Node(4)
    a = Node(5,b,c)
    print(inorder(a))


main()