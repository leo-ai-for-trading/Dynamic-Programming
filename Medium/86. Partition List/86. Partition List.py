# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        
        Reasoning
        - iterate every single elements in the list
        - create 2 different sublist
        - greater or equal value in the right list
        - smaller value in the left list
        - left will become the starter of the new big list, which is the merge of the left and right list and we are going to compare if the value is greater or smaller
        - 
        """
        left, right = ListNode(), ListNode()
        ltail,rtail = left, right
        
        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next
            
        ltail.next = right.next
        #right.next is a dummy node
        rtail.next = None
        return left.next #because left is a dummy node
                
