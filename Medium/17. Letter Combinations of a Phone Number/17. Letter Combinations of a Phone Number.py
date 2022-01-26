class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        
        Reasoning:
        each number is map to some characters
        23 = 9 because 2 = abc and 3 = def, so 3*3 = 9
        backtrack problem because we need to find all the possible combinations
        need to create an hasmap that from every digits corrispond to three letters
        O(n*4^n) because for 9 we have wxyz
        """
        res = []
        digitToChar = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"qprs",
            "8":"tuv",
            "9":"wxyz", 
        }
        def backtrack(i,curStr):
            if len(curStr)==len(digits): 
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
        if digits: #we re doing because they want the output in case of empty string as like this [] and not this [""]
            backtrack(0,"")
        return res  
