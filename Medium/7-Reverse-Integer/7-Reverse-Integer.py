class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #we compute the mode division by 10 of the input and store the one digit 123 % 10 = 3
        #we compute the integer division 123 / 10 = 12
        #compute the mod division by 10: 12 % 10 = 2
        #we multiplu the 3 by 10 because we want to shift the 3 to the left by one and add the 2 from the previous point and we get 32
        #same procedure works for negative number
        #if the values go out of the bound, like -2 ^(31)
        #reverse the input but not the last digit and if the reverse value match the input without the last digit and if the last digit of the reverse input is greater than the last digit of the input we do return 0 -> this needed to check if you go out of bounds
        
        #those one are the bounds
        MIN = pow(-2,31)   #-2147483648 #-2^31
        MAX = pow(2,31)-1  #2147483647 #2^31-1
        
        res = 0
        while x:
            digit = int(math.fmod(x,10)) 
            x = int(x / 10)
            #regarding the first condition because we don't want the last digit; the latest                     #condition will return the last digit of MAX, which is 7
            if (res > MAX // 10 or 
                (res == MAX // 10 and digit >= MAX % 10)): 
                return 0 #because the result is gonna overflow
            if (res < MIN // 10 or 
                (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            res = (res * 10) + digit
        return res
