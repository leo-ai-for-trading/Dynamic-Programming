class Solution:
    def canWinNim(self, n: int) -> bool:
        return mod(n,4) != 0
