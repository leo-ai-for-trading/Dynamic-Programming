# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #if root is None: return []
        def dfs(root,sol):
            if root is None: return []
            dfs(root.left,sol)
            sol.append(root.val)
            dfs(root.right,sol)
            
            return sol
        return dfs(root,[])
