class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        
        Reasoning
        - k indicates the last k-th nodes and split od the linked list 
        - the remainder of the linked list will be put at the end of the list
        - counting from the end of the list (backward)
        - pointer at the tail node
        - shift nodes: (lenght-k-1) because we are starting at the beginning of the list
        - set last pointer to the one to swap nodes
        - k = len(list) means that we are doing no rotation
        - k > len(list) means that we are doing 0 rotation + the surplus of the len(list)
        - O(n)
        """
        if not head:
            return head
        #get lenght
        lenght, tail = 1, head
        while tail.next:
            tail = tail.next
            lenght += 1
        k = k % lenght
        if k == 0:
            #no rotation
            return head
        #move to the pivot and rotate
        cur = head
        for i in range(lenght- k -1):
            cur = cur.next
        newHead=cur.next
        cur.next = None #lenght of the linked list
        tail.next = head #beginning of the list
        return newHead
        
