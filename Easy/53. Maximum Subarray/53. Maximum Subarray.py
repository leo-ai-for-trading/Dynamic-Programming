class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Reasoning
        - O(n)
        - remove the negative shifter
        - increment the pointer
        '''
        maxSub = nums[0] #inizialize the array
        curSum = 0
        for n in nums:
            #compute the max that we can and now
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
    
