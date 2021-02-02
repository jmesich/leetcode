#Increasing Order Search Tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #if we have null then return bc there is no tree
        if not root:
            return
        #helper method
        def helper(root, results):
            #if we have null root then return 
            if not root:
                return
            #call it on the left part of the tree
            helper(root.left, results)
            #add the left parts to the array
            results.append(root.val)
            #call it on the right hand 
            helper(root.right, results)
            return results
        
        array = helper(root, [])
        root = cur = TreeNode(array[0])
        for i in range(1, len(array)):
            cur.right = TreeNode(array[i])
            cur = cur.right
        return root
        
