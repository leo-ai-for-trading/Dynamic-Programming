class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        
        Reasoning
        -  add 1 to last digit
        - edge case: 999, if you add 1 it becomes 9910, but the output must be 1000
        - O(n)
        
        """
        digits = digits[::-1] #reverse to avoid edge case
        one, i = 1, 0
        while one == 1:
            if i < len(digits):
                #inbound
                if digits[i] == 9:
                    #edge case
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                #out of bounds
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1]
