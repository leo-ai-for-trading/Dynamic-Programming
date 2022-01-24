class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window technique
        #our window do not have to contain duplicates so we need to eliminate the duplicates
        #we eliminate the first element of the duplicates 
        #we use set for the substring so we'll know automatically if it contains duplicate 
        #we shrink the window from the left, so we eliminate the duplicates by the first elements
        #O(n) for time and space complexity
        #we need to store the longest substring we will found
        charSet = set()
        left = 0
        ans = 0
        for right in range(len(s)):
            while s[right] in charSet: #means that is a duplicate
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            ans = max(ans,right-left+1)
        return ans
            
