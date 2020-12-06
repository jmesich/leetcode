#Populating Next Right Pointers in Each Node II
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        #checks if it is a null tree
        if not root:
            return root
        #add the root to the queue
        queue = collections.deque([root])
        #while there is something in the queue
        while queue:
            #find the size of Q
            size = len(queue)
            #loop through everything in Q
            for i in range(size):
                #take the first from the queue
                node=queue.popleft()
                #set the queue to the next value
                #in the first case this is null
                #since you add the left one first you will always get the next value
                if i<size-1:
                    node.next=queue[0]
                #append the two children if they are there
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
        
