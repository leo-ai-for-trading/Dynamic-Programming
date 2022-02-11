class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        
        Reasoning
        - if the rectangles are going to extend to the right, but the one on the right is smaller, it means that we have to pop the highest rectangle, because it is the boundary
        - pop from the top to the bottom, from the most recent
        - using stack that cointain the most recent 
        - if the rectangles increase in ascending order we don't need to pop 
        - if the next rect is greater than the previous rect -> pop it, but store the area
        - update the max area only if it is greater than the previous area
        
        
        """
        maxArea = 0
        stack = [] #pair: (index, height)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                #pop the height
                #and extend the current height
                index, height = stack.pop()
                maxArea = max(maxArea,height * (i - index))
                #i - index is the width
                start = index
            stack.append((start,h))
        for i,h in stack:
            maxArea = max(maxArea,h*(len(heights)- i))
        return maxArea
