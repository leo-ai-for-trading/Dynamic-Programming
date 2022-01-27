class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        
        Reasoning
        - in-place: without allocating in another array
        - pointer that will tell us when to replace the duplicate instead of the new value and shift the pointers to 1 on the right
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                #perform the swap
                #partition algo
                nums[k] = nums[i]
                k += 1
        return k
