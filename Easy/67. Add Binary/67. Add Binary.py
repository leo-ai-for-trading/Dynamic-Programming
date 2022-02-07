class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        
           
        """
        res = ""
        carry = 0
        #starting at the end
        a,b = a[::-1],b[::-1]
        for i in range(max(len(a),len(b))):
            #if a in bound
            digit_a = ord(a[i]) - ord("0") if i < len(a) else 0 
            digit_b = ord(b[i]) - ord("0") if i < len(b) else 0
            #convert letter into integer
            
            total = digit_a + digit_b + carry
            char = str(total % 2)
            
            res = char + res
            carry = total / 2
        if carry: #edge case where carry = 0 and carry = 1
            res = "1" + res
        return res
