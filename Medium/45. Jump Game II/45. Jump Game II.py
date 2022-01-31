class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        - min number of jumps to reach the index
        - greedy algorithm -> O(n)
        - search tree
        - breadth first search find min path
        '''
        
        res = 0
        l = r = 0
        #telling us the start of the window
        #left is the left portion of the window and right is viceversa
        while r < len(nums) -1:
            farthest = 0
            #who can jump the farthest
            for i in range(l,r + 1):
                farthest = max(farthest, i + nums[i])
                #i + nums[i] is the farthest jump
            l = r + 1
            r = farthest
            res += 1 #telling us how many jumps
        return res
        
        
      
