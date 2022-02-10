class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        Reasoning
        - not a permutions, it is a subset
        - O(n*2*n) cause of the constraints of the problems
        - 
        """
        res = []
        subset = []
        def dfs(i):
            #i is the index of the value which we are making decision on
            if i >= len(nums):
                res.append(subset[:])
                return #out of bounds
            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)#left branch of the tree
           #decision not to include nums[i]
            subset.pop()
            dfs(i + 1)
            
        dfs(0)
        return res
        
