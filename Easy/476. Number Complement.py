"""
If we xor a number for a mask with all its bits set to 1 and its bit-length equal the the first number length, we get the complement of the first number. Let's make an example:
13 in binary is 1101
Its binary length is 4 so we need to xor 1101 (13) by 1111 (15). The result (the complement) is 0010 (2).
How to get the mask? We simply calculate the index of the most significant bit of the number (3 in the case of 13) and then mask = 2^(MSB+1)-1. Infact 2^(3+1)-1 = 16 - 1 = 15 (1111)

"""
class Solution:
    def findComplement(self, num: int) -> int:
	    # len(bin(num)[2:]) returns the index of the MSB increased by one
        return ((1 << len(bin(num)[2:])) - 1) ^ num
