class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        
        Reasoning
        - compare char by char
        - if chars are equal means we can say that i +1 and j+1 is the new problems, we switch pointers
        - when we insert we are not going to add anything to i, but we add 1 to j
        - when we delete: (i+1, j)
        - replace: (i+1,j+1)
        - if w1[i] = w2[j] -> (i+1,j+1)
        - bottom up dynamic programming
        
        """
        cache = [[float("inf")]*(len(word2) +1) for i in range(len(word1)+1)] #2D array +1 to handle base case
        
        #initialize base cases
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i
            
        #bottom up DP
        for i in range(len(word1) -1, -1, -1):
            for j in range(len(word2) -1,-1,-1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i +1][j +1]
                else:
                    cache[i][j] = 1 + min(cache[i + 1][j],cache[i][j+1], cache[i+1][j+1])
        return cache[0][0]
