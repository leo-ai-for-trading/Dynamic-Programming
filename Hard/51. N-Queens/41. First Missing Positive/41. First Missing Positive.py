class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        '''
        Reasoning
        - nlogn
        - convert input into hashset to brute force it
        - use input array as extra memory
        - negative number are useless, so we replace them with 0 -> O(n)
        - we're taken the abs value of negative number - 1
        '''
        for i in range(len(A)):
            if A[i] < 0:
                A[i] = 0 #neutralize negative value
        for i in range(len(A)):
            val = abs(A[i]) 
            if 1 <= val <= len(A): #values in bound
                
                if A[val - 1] > 0:

                    A[val - 1] *= -1
                elif A[val - 1] == 0:
                    A[val -1] = -1 * (len(A) + 1)
        for i in range(1, len(A)+1):
            if A[i - 1] >= 0:
                #means i never shows in A
                return i
        return len(A) + 1
