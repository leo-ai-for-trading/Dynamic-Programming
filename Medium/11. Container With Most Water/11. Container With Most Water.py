class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #check every right pointer and left pointer
        #max the area is the scope
        #the left pointer is the first figure and the right the latest one
        #i'm gonna shift the min(pointer), that could be the right pointer or the left pointer, in case they are the same it doies not matter which one you shift
        
        #l: left
        #r: right
        res = 0
        l,r = 0, len(height)-1
        
        while l < r:
            area = (r- l)*min(height[l],height[r])
            res = max(res,area)
            if height[l] < height[r]: #max the area
                l +=1
            else:
                r -= 1 
        return res
