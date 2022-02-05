class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        Reasoning
        - mod by, % 10 to get the second digit
        - divide by 10, / 10, to get the first digit
        - O(n+m) time complexity
        - O (n*m) space complexity
        '''
        if "0" in [num1,num2]:
            return "0"
        res = [0]* (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        #reverse string 
        
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                
                res[i1 + i2] += digit  #add first digit
                #what position to put in the output
                
                res[i1 + i2 + 1] += (res[i1 + i2] // 10) 
                res[i1 + i2] = res[i1 + i2] % 10
                #get second digit
        res, begin = res[::-1], 0
        while begin < len(res) and res[begin] == 0:
            begin += 1
        res = map(str, res[begin:]) #convert all values from the begin
        return "".join(res)
