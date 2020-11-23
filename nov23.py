#House Robber III
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def moddedDFS(root):
            #if the root is empty then we want to return 0,0 as we found a leaf
            if not root:
                return (0, 0)
            #go into each branch of the binary tree
            left_branch, right_branch = moddedDFS(root.left), moddedDFS(root.right)
            #returns two values
            #first is the root value plus the right branchs of each child
            #the other is the max values of both
            return (root.val + left_branch[1] + right_branch[1], max(left_branch) + max(right_branch))
        
        return max(moddedDFS(root))
