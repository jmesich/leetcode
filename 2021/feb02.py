# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        # should be recursive
        # if there is a number outside the bounds,
            # find the next available node
            #if none , put null
        def trimBST_helper(root,low,high): 
            if root == None: 
                return None
      
            # First fix the left and right subtrees of root  
            root.left = trimBST_helper(root.left, 
                                   low, high)  
            root.right = trimBST_helper(root.right, 
                                    low, high)  
      
            # Now fix the root. There are 2 
            # possible cases for toot  
            # value is too small 
            if root.val < low: 
                return root.right   

            # value is too big 
            if root.val > high: 
                return root.left  

            # root is in range  
            return root 
        return trimBST_helper(root,low,high)
