class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #start in the middle and expand outwords in both directions
        #O(n^2)
        #the even palindrome is an edge case
        
        ans = ""
        ansLen = 0
        
        for i in range(len(s)):
            #odd lenght
            left ,right = i, i #this is the center position
            while left >= 0 and right < len(s) and s[left] == s[right]:
                #the last condition tells me if it is palindrome
                if (right - left + 1) > ansLen: #lenght of the palindrome
                    ans = s[left:right+1] #update result
                    ansLen = right-left+1
                left -= 1
                right += 1
                
            #even lenght
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right-left+1) > ansLen:
                    ans = s[left:right+1]
                    ansLen = right -left + 1
                left -= 1
                right += 1
        return ans
