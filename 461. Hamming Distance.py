class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = bin(x ^ y) # binary rapresentation
        return xor.count('1') # xor result will be 1 if bits are different at that index
