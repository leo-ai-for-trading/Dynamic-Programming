# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Reasoning
        - for each node, first the node is visited and then it's child nodes are put in a FIFO, first in first out, queue
        - implement a queue as a linked list
        - BFS and add the value into list
        - 
        '''
        res = []
        q = collections.deque() #queue
        q.append(root)
        while q:
            qlen = len(q)
            lev = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    lev.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if lev:
                res.append(lev)
        return res
