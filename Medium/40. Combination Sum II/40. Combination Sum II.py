class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Reasoning
        - O(n^2)
        - if the value in the list is greater than the target we skip the value
        - if the sum of the nodes is greater than the target the solution we'll be not available 
        - pointer i on the left
        - sorted the input array  

        '''
        
        candidates.sort()
        res = []
        def backtracking(cur, pos, target):
            if target == 0:
                #reached the base case
                res.append(cur.copy())
            if target <= 0:
                return 
            prev = -1 #this allows to not execute as the first iteration 
            for i in range(pos,len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtracking(cur,i+1,target-candidates[i])
                cur.pop()
                
                prev = candidates[i]
        backtracking([],0,target)
        return res
