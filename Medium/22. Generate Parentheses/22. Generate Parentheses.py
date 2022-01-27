class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        
        Reasoning
        always start with closing parenthesis is invalid
        we could start only with open parenthesis
        after 1 pair of open and closed parenthesis needs to. be followed by open parenthesis
        we could only add closing parenthesis if the count of closed parenthesis is less than the open parenthesis
        we can add as many opened parenthesis as we want
        backtrack solution
        valid IIF open == closed == n
        """
        stack = []
        res = []
        
        def backtrack(openN,closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN +1,closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN,closeN+1)
                stack.pop()
        backtrack(0,0)
        return res
        
