class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Reasoning
        - output: how many unique values you have in the array
        - the first unique value we re going to put as the first element of the new value and the second unique value as the second element etc
        - the second unique value needs to be in the second position and so on
        - left pointer will be the position of the next unique value
        -  the right pointer will scan the array
        the left pointer takes care of the unique value, the output parameter
        - we increment the left pointer
        - compare the value with the previous value to check if it is the first time we are seing that value
        - O(n)
        """
        l = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                #comparing values
                nums[l] = nums[r]
                #now we have unique value
                l += 1
        return l
