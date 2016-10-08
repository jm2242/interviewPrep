__author__ = 'jonathanmares'


class Node:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next_node = next_node


def deletedups(l):
    dict = {}

    if not (l or l.next_node):
        return l

    dict[l.val]  = True
    prevNode = l
    currentNode = l.next_node
    while currentNode:
        try:
            if dict[currentNode.val]:
                prevNode.next_node = currentNode.next_node
                print('found a duplicate')
        except:
            dict[currentNode.val] = True
            prevNode = currentNode

        currentNode = currentNode.next_node
    return l




def printList(startNode):
    while startNode:
        print(startNode.val)
        startNode = startNode.next_node

def kthToLast(startNode, k):
    pointerOne = startNode
    print(pointerOne.val)
    pointerTwo = startNode
    lengthOfList = 1
    while (pointerOne.next != None):
        lengthOfList += 1
        pointerOne = pointerOne.next

    if lengthOfList < k:
        return None

    movesToGo = lengthOfList - k
    while (movesToGo):
        movesToGo -= 1
        pointerTwo = pointerTwo.next






def main():
    node1 = Node(5,None)
    node2 = Node(5, node1)
    node3 = Node(10, node2)
    node4 = Node(15, node3)
    node5 = Node(10, node4)

    kthToLast(node5, 2)

main()


