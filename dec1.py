# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #if the root is none then we have found the end
        if root is None: 
            return 0 ;  
        # we want to continue to traverse the tree
        else : 
            # Compute the depth of each subtree 
            left_d = self.maxDepth(root.left) 
            right_d = self.maxDepth(root.right) 
  
            # find which side is bigger 
            if (left_d > right_d): 
                return left_d+1
            else: 
                return right_d+1
        
