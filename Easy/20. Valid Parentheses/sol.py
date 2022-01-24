class Solution:
    def isValid(self, s: str) -> bool:
        #we can't start with closes parenthesis
        #we need to start with open parenthesis and they could be follow with open parenthesis
        #using stack data structure: because the closed parethensis must matched the one before it and the moment when the match you're gonna pop them out from the stack and if the list the end it will be return True
        #O(n) 
        stack = []
        closeToOpen = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in closeToOpen: #means that is a closed parenthesis
                    if stack and stack[-1] == closeToOpen[c]:
                        stack.pop()
                    else:
                        return False 
            #because parenthesis are not matched like (]
            else:
                stack.append(c)
        return True if not stack else False
    #mean that i return true if the stack is empty
