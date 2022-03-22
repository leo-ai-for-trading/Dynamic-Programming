# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #find the insertion point of a new element x; the function return the first index i such that tab[i] >= x
        return bisect_left(range(n),True,1,key=isBadVersion)
