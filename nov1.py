#Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        #convert to list
        value_list=[]
        value=0
        while head!= None:
            value_list.append(head.val)
            head=head.next
        print(value_list)
        print(len(value_list))
        #value * 2 ^ len(list-k)
        for k in range(len(value_list)):
            value= value + value_list[k]*2**(len(value_list)-k-1)
        
        return value
