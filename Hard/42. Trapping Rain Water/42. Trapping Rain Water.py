class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Reasoning
        - min(L,R) - h[i] >= 0 menas how much water we can trap in position i
        - O(1)
        -  
        '''
        if not height: return 0
        l, r = 0, len(height) -1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            #before they meet each other
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
                
