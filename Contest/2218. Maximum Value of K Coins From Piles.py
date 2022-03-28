"""
There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

Solution
dp[i,k] means picking k elements from pile[i] to pile[n-1].
We can pick 0,1,2,3... elements from the current pile[i] one by one.
It asks for the maximum total value of coins we can have,
so we need to return max of all the options.
"""
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @functools.lru_cache(maxsize=None)
        def dp(i,k):
            if k == 0 or i == len(piles): return 0
            res, cur = dp(i + 1,k),0
            for j in range(min(len(piles[i]),k)):
                cur += piles[i][j]
                res = max(res,cur + dp(i + 1, k - j - 1))
            return res
        return dp(0,k)
