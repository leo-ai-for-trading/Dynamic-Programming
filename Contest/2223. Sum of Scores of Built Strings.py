"""
Actually, what is asked to find in this problem is famous z-function. For more details please see https://cp-algorithms.com/string/z-function.html. If you know this algorithm, this problem is a piece of cake. If you not, it becomes much more difficult.

"""
class Solution:
    def sumScores(self, s):
        def z_function(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1
            return z
        
        return sum(z_function(s)) + len(s)
