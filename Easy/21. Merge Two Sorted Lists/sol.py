# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #extract first one and compare them
        #go to the next node
        #build dummy node in the output list to avoid edge cases of the initial empty list
        #the dummy will be 1
        #now we analyze each nodes of the two lists and put the smallest in the output 
        #if we've got remain nodes we need to sort them and take that portion and put into the output
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2: #they need to be not empty
            if list1.val < list2.val: 
                tail.next = list1
                list1 = list1.next #check new node
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        if list1:
            tail.next = list1 #take the portion of the list and put into the tail
        elif list2:
            tail.next = list2
            
        return dummy.next
