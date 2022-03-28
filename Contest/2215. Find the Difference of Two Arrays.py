"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        s1 = set(nums1)
        s2 = set(nums2)
        nums1 = list(s1)
        nums2 = list(s2)
        s = []
        d = []
        for i in range(len(nums1)):
            if nums1[i] not in s2:
                s.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in s1:
                d.append(nums2[i])
        res.append(s)
        res.append(d)
        return res
