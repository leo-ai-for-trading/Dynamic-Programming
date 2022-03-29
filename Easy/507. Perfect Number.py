class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        for p in 2,3,5,7,13:
            if 2**(p-1) * (2**p - 1) == num:
                return True
        return False
