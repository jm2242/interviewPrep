    #     for idx, root in enumerate(nodes):
    #         # if len(nodes[:idx]) == 1 and len(nodes[idx+1:]) == 1:
    #         #     validTrees.append(1)
    #         #     continue
    #         print "root is : {0}".format(root)
    #         # left children
    #         self.builder(root, nodes[:idx], validTrees)
            
    #         # right children
    #         self.builder(root, nodes[idx+1:], validTrees)
        
    #     return len(validTrees)
            
    
    # def builder(self, parent, nodes, validTrees):
    #     #print "parent is: {0}".format(parent)
        
    #     if not nodes:
    #         return 
        
    #     # if we have one node, then there is only one way to make a tree
    #     if len(nodes) == 1:
    #         validTrees.append(1)
    #         print "validTrees: {0}".format(validTrees)
    #         print parent,nodes
            
    #     # otherwise send nodes to left and right children to see how many
    #     # trees can be made
        
    #     for idx, root in enumerate(nodes):
    #         if len(nodes[:idx]) == 1 and len(nodes[idx+1:]) == 1 and nodes[:idx] < parent and nodes[idx+1:] > parent:
    #             print "nodes: {0}".format(nodes)
    #             validTrees.append(1)
    #             continue
    #         print "root: {0}, last node: {1}".format(root, nodes[-1])
    #         # left children

    #         self.builder(root, nodes[:idx], validTrees)
            
    #         # right children

    #         self.builder(root, nodes[idx+1:], validTrees)