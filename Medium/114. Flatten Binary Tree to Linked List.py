"""
Given the root of a binary tree, flatten the tree into a "linked list":
"""

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            currentRight = root.right
            root.right = root.left
            
            dummy = root
            while dummy.right:
                dummy = dummy.right
            dummy.right = currentRight
            
            root.left = None
            self.flatten(root.right)
