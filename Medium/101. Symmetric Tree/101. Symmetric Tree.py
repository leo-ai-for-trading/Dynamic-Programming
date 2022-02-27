# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
        Reasoning
        - their root node must be the same
        - left subtree of left tree and right subtree of right tree have to be mirror images
        - right subtree of left tree and left subtree of right tree have to be mirror images
        - return bool
        '''
        def isMir(r1,r2):
            #edge case
            if r1 is None and r2 is None:
                return True
            if (r1 is not None and r2 is not None):
                if r1.val == r2.val:
                    return (isMir(r1.left,r2.right)and (isMir(r1.right,r2.left)))
            return False
        return isMir(root,root)
