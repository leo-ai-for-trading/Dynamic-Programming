import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        test = "abcdefghijklmnopqrstuvwxyz0123456789"
        ans = ""
        for i in s:
            if i in test:
                ans += i
        return True if ans == ans[::-1] else False
