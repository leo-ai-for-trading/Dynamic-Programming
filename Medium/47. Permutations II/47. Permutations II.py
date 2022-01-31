class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        Reasoning
        - this contain duplicates
        - backtracking
        - modify array in hashmap
        '''
        res = [] 
        perm = []
        count = {n:0 for n in nums} #map to 0
        for n in nums:
            count[n] += 1
        
        def depthresearch():
            if len(perm) == len(nums):
                #no add remain
                res.append(perm.copy())
                #we make copy because we are changing the variable
                return
        
            for n in count:
                #every key in the hasmap in unique
                if count[n] > 0: #means we have enough values left
                    perm.append(n)
                    count[n] -=1

                    depthresearch()

                    count[n] += 1
                    perm.pop()

        depthresearch()
        return res
