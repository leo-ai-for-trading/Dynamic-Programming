class Solution:
    def toHex(self, num: int) -> str:
        to_hex = "0123456789abcdef"
        
        if num == 0:
            return "0"
        elif num < 0:
            num += 2 ** 32
        
        ans = []
        while num:
            ans.append(to_hex[num & 15])
            num >>= 4
        
        return ''.join(ans[::-1])
