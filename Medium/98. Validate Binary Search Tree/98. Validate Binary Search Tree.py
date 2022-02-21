# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        Reasoning
        -  every value in the subtree in the left will be smaller and in the right will be strictly greater than the node
        - dfs approach: brute force to check if every value meet the requirements
        - update right bounday when we check the left child and viceversa when we check the right child
        - 
        '''
        def valid(node, l, r):
            if not node:
                return True
                #empty bst is still bst, bst is binary search tree
            if not (node.val < r and node.val > l):
                return False
            
            return (valid(node.left, l, node.val) and valid(node.right, node.val, r))
        
        return valid(root, float("-inf"),float("inf"))
