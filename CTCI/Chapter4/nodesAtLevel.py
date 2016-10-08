from Queue import *

class Node:
    # children -> a list of children
    def __init__(self, value, children):
        self.value = value
        self.children = children    
    def __str__(self):
         return self.value
   


def list_nodes(root):
    # list for storing nodes at each level, where level=index
    return_ary = []

    # create queue
    queue = Queue()
    
    # push root onto queue
    queue.put(root)
    
    # perfrom a BFS
    while not queue.empty():
        # keep track of nodes at current leve
        adding_nodes = queue.qsize()
        print "Number of nodes at current level {0}".format(adding_nodes)

        # nodes at each level
        nodes_at_level = []

        # loop for number of nodes at each level 
        for x in range(0,adding_nodes):
            node = queue.get()
            nodes_at_level.append(node.value)
            for y in node.children:
                queue.put(y)
        return_ary.append(nodes_at_level) 
    return return_ary
    

def main():
    
    d = Node("d",[])    
    c = Node("c",[])
    b = Node("b",[])    
    a = Node("a",[d])    
    root = Node(0,[a,b,c])

    print list_nodes(root)
    
    
main()