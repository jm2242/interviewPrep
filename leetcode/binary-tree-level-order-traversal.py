from Queue import Queue
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # General Approach: BFS, storing level along with node
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levelOrder = []
        if not root:
            return []
        
        currentLevel = 0
        currentLevelOrder = []
        q = Queue()
        q.put( (root, 0) )
        
        
        while not q.empty():
            
            # get item from queue
            node, level = q.get()
            # print "visiting node {0} at level {1}".format(node.val, level)
            
            # check if we are the next level
            if currentLevel < level:
                # print "next level"
                # send off currentLevel and reset it for this level
                levelOrder.append(currentLevelOrder)
                # print "level order is now: {0}".format(levelOrder)
                currentLevelOrder = []
                currentLevel += 1
            
            # add node to current level
            currentLevelOrder.append(node.val)
            
            for child in [node.left, node.right]:
                if child is None:
                    continue
                else:
                    q.put( (child, currentLevel+1) )
                    
        # finished traversing, store the last level's traversal
        levelOrder.append(currentLevelOrder)
        
        return levelOrder
                
            
            
            
            
            
            