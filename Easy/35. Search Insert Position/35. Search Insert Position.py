class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        Reasoning
        - input is sorted
        - O(logn) >> O(n)
        - binary search method: 
            - left pointer, right pointer, compute the middle
            - expand the middle
            - start searching to the right, so shift left pointer
            - recompute middle pointer
            
        """
        l,r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                #searching to the right
                l = m+1
            elif target < nums[m]:
                r = m-1
        return l #if the target does not exist
                
        
