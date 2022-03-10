class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1 + nums2
        a.sort()
        b = len(a) 
        if a == []:
            return 0
        if len(a) < 2:
            return a[0]
        if (len(a)%2) != 0:
            c = int((b)/2)
            me = a[c]
            return me
        else:
            me1 = a[int((len(a))/2)]
            me2 = a[int(len(a)/2)-1]
            me = (me1 +me2) /2
            return me
            
            
