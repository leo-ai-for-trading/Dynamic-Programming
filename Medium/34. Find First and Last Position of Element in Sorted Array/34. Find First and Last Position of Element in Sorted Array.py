class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        Reasoning
        - could be multiple copies of the target value
        - binary search O(logn)
        - compute the middle value by sum left and right pointers and divide them by 2
        - binary search applying two times
        
        """
        left = self.binarySearch(nums,target,True)
        right = self.binarySearch(nums,target,False)
        return [left,right]
    def binarySearch(self,nums,target,leftBias):
            #leftBias is true or false and if false, the result is rightbiased, means that we re looking for the right most index, otherwise we are looking for the left most index, if it true
        l,r = 0,len(nums)-1
        i = -1
        while l <= r:
                #m: middle
            m = (l+r)// 2 #integer division
            if target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
            else:
                    #find the target value
                i = m
                if leftBias:
                        #looking for the left most value
                    r = m-1
                else:
                        #searching to the right
                    l = m+1
                    
        return i
                    
        
