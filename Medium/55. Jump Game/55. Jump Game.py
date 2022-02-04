class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Reasoning
        - DP problem solved in greedy way
        - can we reach the last position of the list?
        - O(n)
        - the jump will be based on the value of the list: if the value of the list where we are at is equal to 2, we need to make a jump to 2 positions
        - starter point at first position on the left
        '''
        goal = len(nums)-1
        #reached the last index in the array
        for i in range(len(nums)-1,-1,-1):
            #from the beginning to the last index
            if i + nums[i]>= goal:
                #we can reach the goal with this condition
                goal = i
                
        return True if goal == 0 else False
       
