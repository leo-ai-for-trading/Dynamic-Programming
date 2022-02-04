class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        Reasoning
        - we pop the double dots diretory and we only store the "/"
        - start at the left pointers
        - O(n)
        - using stack because of the double dots operator
        - pop the double dots from the stack
        
        '''
        stack = []
        cur = ""#current path or file we are looking at
        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack: stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
                
            else:
                cur += c
                
        #stack = ["abc","def"]
        
        return "/" + "/".join(stack)
               
