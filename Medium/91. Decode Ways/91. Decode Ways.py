class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        Reasoning
        - with DP like fibonacci sequence
        - bottom up approach starting at the end
        '''
        dp = {len(s):1}
        #base case
        
        for i in range(len(s) -1, -1, -1):
            #iterating in reverse order
            if s[i] == "0":
                dp[i] = 0
            else: #digit from 1 to 9
                dp[i] = dp[i+1]
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
        return dp[0]
