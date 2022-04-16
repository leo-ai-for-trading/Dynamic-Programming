class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            if abs(nums[i]) in d:
              #in case of -1 and 1 as answer you need to return 1
                d[abs(nums[i])]=max(d[abs(nums[i])],nums[i])
            else:
              #populate the dict
                d[abs(nums[i])]=nums[i]
        return d[min(d.keys())]
