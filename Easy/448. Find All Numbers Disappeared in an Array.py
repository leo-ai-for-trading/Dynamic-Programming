class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = []
        miss = 1
        for n in nums:
            a.append(miss)
            miss += 1
        s1 = set(nums)
        s2 = set(a)
        s3 = s2.difference(s1)
        return list(s3)
