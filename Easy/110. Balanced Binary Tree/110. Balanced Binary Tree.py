# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        - bottom up 
        - the height of the subtree is 1+max(left,right)
        """
        def dfs(root):
            #return bool and height of the tree
            if not root: return [True,0]
            l,r = dfs(root.left),dfs(root.right)
            balance = (l[0] and r[0] and
                        abs(l[1] - r[1]) <=1)
            return [balance, 1 +max(l[1],r[1])]
        
        return dfs(root)[0]
