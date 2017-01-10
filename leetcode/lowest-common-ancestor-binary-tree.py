# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    # O(1) space solution
    def lca(self, root, p, q):
        if root in (None, p, q):
            return root
            
        leftResult = self.lowestCommonAncestor(root.left, p, q)
        rightResult = self.lowestCommonAncestor(root.right, p, q)
        
        # if we get a non-None value from both children, then we are the LCA
        if leftResult and rightResult:
            return root
        
        # neither p nor q are in the children
        elif leftResult is None and rightResult is None:
            return None
        
        else:
            return leftResult or rightResult
        

    # O(n) space solution
    # General Approach: get the paths to each node, then compare the two paths
    # for the point at which the two paths split
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        
        # if they are the same node
        if p == q:
            return p
        
        
        # get path to both nodes, compare paths
        pathToP = self.getPathToNode(root, p)
        pathToQ = self.getPathToNode(root, q)
        for i in range( min( len(pathToP),len(pathToQ) )):
            if pathToP[i] == pathToQ[i]:
                continue

            # get the last node that was the same, the LCA
            else:
                return pathToP[i-1]
        
        # lowest common ancestor is the last element of either list
        else:
            return pathToQ[i]

    # find a path beginning from root to node
    def getPathToNode(self, root, node):
        
        if root is None:
            return None
        
        if root == node:
            return [node]
            
        leftResult = self.getPathToNode(root.left, node)
        rightResult = self.getPathToNode(root.right, node)
        
        if leftResult is not None:
            return [root] + leftResult
        
        if rightResult is not None:
            return [root] + rightResult
        
        return None
            
        #raise Exception("means that node does not exist in tree")
        