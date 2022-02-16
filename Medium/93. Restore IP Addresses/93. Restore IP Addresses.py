class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        '''
        Reasoning
        - leading zero stands for "01"
        - brute force 
        - backtracking
        - moving the dot create integer until > 255
        - max 3 digits
        - no skip digits cause it is not allowed
        - 
        '''
        res = []
        if len(s) > 12:
            return res
        def backtr(i, dots,curIP):
            '''
            @dots: how many dots we have inserted so far
            @curIP: current string
            '''
            #base case
            if dots == 4 and i == len(s):
                res.append(curIP[:-1])
                return
            if dots > 4:
                return 
            
            for j in range(i, min(i+3, len(s))):
                #avoid out of bounds
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                    backtr(j+1,dots+1, curIP + s[i:j+1]+".")
                    #dots+1 because we are adding 1 dots each time
                    #prevent lead zero by (i==j)
        backtr(0,0,"")
        return res
