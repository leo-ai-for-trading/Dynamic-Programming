"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Reasoning:
        - two loops: the first create copy of nodes
        - second loop create hash map to map the old node in the new node
        """
        oldcopy = { None: None}
        cur = head
        #copy the node
        while cur:
            copy = Node(cur.val)
            oldcopy[cur] = copy
            cur = cur.next
        
        #set the pointer
        cur = head
        while cur:
            copy = oldcopy[cur]
            copy.next = oldcopy[cur.next]
            copy.random = oldcopy[cur.random]
            cur = cur.next
        
        return  oldcopy[head]
