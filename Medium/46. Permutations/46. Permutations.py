class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        Reasoning
        - backtracking solutions
        """
        res = []
        #base case
        if (len(nums) == 1):
            #only one permutation
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            #pop the first element
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
