class Solution:
    def romanToInt(self, s: str) -> int:
        #largest number goes first 
        #smaller goes first if you want to subtract
        #can't put multiple smaller value before the larger 
        #iterate string by string
        #if the next is larger than i'm gonna subtract, viceversa i'm gonna sum them
        #-100 + 1000 -10+100+5+1+1+1 = 998
        #O(n)
        
        rom = {"I":1,
              "V":5,
              "X":10,
              "L":50,
              "C":100,
              "D":500,
              "M":1000} #hashmap
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and rom[s[i]] < rom[s[i+1]]:
                res -= rom[s[i]] #perform subtraction
            else: 
                res += rom[s[i]]
        return res
