class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s is None:
            return 0
        else:

            a = s.split()
            b = a[-1]
            return len(b)
