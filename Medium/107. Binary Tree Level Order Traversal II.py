# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

**using BFS**
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        res = []
        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    temp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if temp:
                res.append(temp)
        return res[::-1]
