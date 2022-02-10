class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        
        Reasoning
        - brute force solution
        - backtracking
        - k is height of the decision tree
        - we do not want duplicates: chose greater value of before to eliminate duplicates
        - 
        """
        res = []
        def backtrack(start, comb):
            #comb: previous value
            if len(comb) == k:
                res.append(comb[:])
                return
            
            #decision tree:
            for i in range(start,n + 1):
                #n+1 to include n
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        backtrack(1,[])
        return res
