#Range Sum of BST
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        left_sum=0
        right_sum=0
        total_sum=0
        if root.left != None:
            left_sum = self.rangeSumBST(root.left,low,high)
        if root.right != None:
            right_sum = self.rangeSumBST(root.right,low,high)
        total_sum= left_sum+right_sum
        if root.val<=high and root.val>=low:
            total_sum=total_sum+root.val
        
        return total_sum
        
            
            
        
