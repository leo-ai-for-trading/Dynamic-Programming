class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Reasoning
        - eliminate duplicate combinations
        - we store the first element in the left node and an empty list on the right node to avoid duplicate
        - the leaves of the node 2 will contain no duplicates on the right nodes
        - pointer on the left to track the element to pop 
        - O(2^target)
        '''
        res = []
        
        def deapthResearch(i,cur,total):
            if total == target:
                #we find the result
                res.append(cur.copy())
                #we want to create a copy to use it again when we do other combinations recursively
                return
            if i>= len(candidates) or total > target:
                return
                #i is out of bound or total is goint out of bound
            
            cur.append(candidates[i])
            deapthResearch(i,cur,total + candidates[i])
            cur.pop() #go for next decision
            deapthResearch(i+1,cur,total)
            #create second branch decision
        deapthResearch(0,[],0)
        return res
        
