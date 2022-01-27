# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        Reasoning
        - create dummy node at the beginning
        - current node ia going to reverse with the previous node
        - i'm gonna swap the previous node with the current node
        - next pointer will go on the node after the current node and the current node after the previous
        -  it will become from 0-1->2->3->4 to 0-2->1->3->4
        - now we re going to swap 1 to swap to 4 and 3 after 4
        - it will become from 0->2->1->3->4 to 2->1->4->3
        - O(n)
        """
        
        dummy = ListNode(0,head)
        prev, curr = dummy, head
        
        while curr and curr.next: #while curr is not the end and the next node is the end 
            #save pointers
            nextPair = curr.next.next
            second = curr.next
            
            #reverse this pair of nodes
            second.next = curr
            curr.next = nextPair
            prev.next = second #second node is put in first position
            #update pointers 
            prev = curr
            curr = nextPair
        return dummy.next
