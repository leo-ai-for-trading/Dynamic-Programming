# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        
        Reasoning
        - singly linked means that there is a pointer going out from every single node
        - no 0 index like arrays
        - reversing from left to right: means that left = null and break that link
        - our first node we want to point out the node after the right node
        - dummy node
        - first: getting the pointer to reach the left node -> iterate L - 1 and shifting current pointer by one and also shift p by one
        - second: iterate (right - left + 1) -> taking cur and assigned to next node
        - third: update pointers
        """
        #phase 1: reach node at position left
        dummy = ListNode(0, head)
        leftprev, cur = dummy, head
        for i in range(left - 1):
            leftprev, cur = cur, cur.next
            
        #now cur = ledt, leftprev = node before left
        #reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tempnext = cur.next
            cur.next = prev
            prev, cur = cur, tempnext
            
        #update pointers
        leftprev.next.next = cur #cur is node after right
        leftprev.next = prev #prev is right
        return dummy.next
