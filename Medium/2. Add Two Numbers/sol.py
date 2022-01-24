# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #sum elements in lists by iterating two lists first: 5->6->4 and 2->4->3->3 we re going to sum 5 with 2 and so on and we start at the beginning of each list because they are sorted in reverse order nad if a list contains more elements than the order one so we re going to presume that the missing element will be 0 
        dummy = ListNode() #to not deal with edge cases of inserting in two linked lists
        cur = dummy #current position
        carry = 0 
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            #compute new digit
            val = v1+v2+carry
            #if we have two digits number like 23
            carry = val // 10
            val = val % 10 #will give us the 2 of 23
            cur.next = ListNode(val)
            
            #update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        #the condition on line 12 "...or carry is about the number will be for example 15, so the carry will be 1, but the v1 and v2 will be 0 and i want to continue the loop anyway. This last case in an edge case"
            
        return dummy.next
