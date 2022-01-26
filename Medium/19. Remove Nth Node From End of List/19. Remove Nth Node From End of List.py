# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        
        Reasoning: 
        add dummy node at the beginning and we initialize the left pointer at the dummy node and the right pointer to nodes ahead so when we shift the left node will reach the node before the one we would lile to remove and the right pointer will shift into Null node and we re going to shift the left pointer to the last nodes
        """
        dummy = ListNode(0,head)
        l = dummy
        r = head
        
        while n > 0 and r:
            r = r.next
            n -=1 #shifting right pointer
            
        while r:
            l = l.next
            r = r.next
        #let's delete the node
        l.next = l.next.next
        #1 ->2 -> 3
        #become 1->3
        return dummy.next
