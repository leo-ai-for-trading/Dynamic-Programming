"""
Goals: return the single element of triangular sum

We can see from the image that we will sum up the first cell and the second cell. 
Then, since it's triangular, the length of the top row is greater (+1) than the next row.
"""
class Solution:
  def triangularSum(self, nums: List[int]) -> int:
    n = len(nums)
    while n > 0:
      for i in range(n-1):
        nums[i] = (nums[i] + nums[i+1]) % 10
      n -= 1
    return nums[0]

