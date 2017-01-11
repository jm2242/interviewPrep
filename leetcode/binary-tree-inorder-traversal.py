from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # itterative solution - Tushar's way
        
        if not root:
            return []
        
        stack = []
        visitPath = []
        
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
                
            elif root is None:
                # if stack is empty then we are done here
                if not stack:
                    break
                
                root = stack.pop()
                visitPath.append(root.val)
                root = root.right

        return visitPath
    
    '''
     # itterative solution - my way
     # O(n + h) space, where h is the height of the tree
     O(n) factor comes from the visited dictionary
    '''
    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # recursive solution
        # traversal = []
        # self.helper(root, traversal)
        # return traversal
        
        
        
        if not root:
            return []
        
        
        stack = []
        visited = defaultdict(lambda: False)
        visitPath = []
        
        stack.append(root)
        
        while stack:
            
            node = stack.pop()
            
            # check for left children
            if node.left is not None and not visited[node.left]:
                print "checking left children"
                # push node back onto stack
                stack.append(node)
                
                # put left child on stack
                stack.append(node.left)
                
                continue
            
            # visit the node 
            visitPath.append(node.val)
            
            # mark that we visited this node
            visited[node] = True
            
            # check for right children
            if node.right is not None:
                
                # put left child on stack
                stack.append(node.right)
        
        return visitPath
                
                
            
            
            
            
            
                
            
        
        
    
    
    
    
    def helper(self, root, traversal):
        
        if root is None:
            return
        
        if root.left is not None:
            self.helper(root.left, traversal)
        
        traversal.append(root.val)
        
        if root.right is not None:
            self.helper(root.right, traversal)
            
        return
        
        