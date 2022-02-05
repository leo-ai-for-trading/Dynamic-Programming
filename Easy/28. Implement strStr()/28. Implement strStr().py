class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        Reasoning
        - O(n*m) where m is the lenght of the needle
        '''
        if needle == "":
            return 0
        for i in range(len(haystack) + 1- len(needle)):
            #with this we starting with first position and at the first "l", like "hello"
            #we are going to start on "h" and finish on "l"

            if haystack[i: i + len(needle)] == needle:
                return i
                    
        return -1
