# Insertion Sort List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        #Make the first node the start of the sorted list.
        sortedList= head
        current = head.next
        sortedList.next= None
        while current != None:
            node = current
            current=current.next
            if node.val<sortedList.val:
                #Advance the nodes
                node.next= sortedList
                sortedList= node
            else: 
                #Search list for correct position of current.
                search= sortedList
                while search.next!= None and node.val > search.next.val:
                    search= search.next
                #current goes after search.
                node.next= search.next
                search.next= node
        return sortedList
            
        
