# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            i = inorder.index(postorder.pop())
            node = TreeNode(inorder[i])
            node.right = self.buildTree(inorder[i+1:],postorder)
            node.left = self.buildTree(inorder[:i],postorder)
            return node
