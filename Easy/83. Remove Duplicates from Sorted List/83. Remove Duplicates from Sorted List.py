
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        Reasoning
        - to remove duplicate we use pointers
        - the list is sorted so we do not need the dummy node
        - never removing the head but the after if it is duplicated
        - cur: corrent node
        - 
        """
        cur = head
        while cur:
            #until it is Null
            while cur.next and cur.next.val == cur.val:
                    #we need to delete
                    cur.next = cur.next.next
            cur = cur.next
                
        return head
