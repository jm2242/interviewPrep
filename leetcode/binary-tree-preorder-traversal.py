# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    Itterative solution
    Main idea: Vist ourselves first
    Use stack to store right children, pop off root is None
    Recurse down left child
    '''
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
            
        stack = []

        # path
        visitPath = []
        
        while True:
            if root is None:
                if not stack:
                    break
                
                root = stack.pop()
            else:
                # add ourselves to path
                visitPath.append(root.val)
                
                # push the right child on the stack
                stack.append(root.right)
                
                # recurse down left child
                root = root.left
                
        
        
        return visitPath
            
        
        
        
  
    # recursive solution
    def preorderTraversalRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        traversal = []
        if root is None:
            return traversal
        self.helper(root, traversal)
        return traversal
        
    def helper(self, root, traversal):
        
        if root is not None:
            traversal.append(root.val)
        
        if root.left:
            self.helper(root.left, traversal)
        
        if root.right:
            self.helper(root.right, traversal)
        
        