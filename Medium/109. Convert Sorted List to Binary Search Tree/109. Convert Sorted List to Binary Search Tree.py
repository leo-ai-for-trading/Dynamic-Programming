# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        it = head
        l = []
        while it:
            l.append(it.val)
            it = it.next
            #using recursion
        def help(l):
            if not l:
                return None
            mid = len(l)//2
            node = TreeNode(l[mid])
            node.left = help(l[:mid:])
            node.right = help(l[mid+1::])
            return node
        node = help(l)
        return node
