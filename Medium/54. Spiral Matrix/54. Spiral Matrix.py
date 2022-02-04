class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        Reasoning
        - sub-rectangle in the middle of the array
        - shrink the pointers
        - 4 pointers: left, right, top and bottom
        - start at the top left position
        - output is a list 
        - if the pointers will be in the same position that'll be the end of the algorithm
        - O(n*m)
        '''
        res = []
        l,r = 0,len(matrix[0])
        top, bottom = 0,len(matrix)
        
        while l < r and top < bottom:
            #get every i in the top row
            for i in range(l,r):
                res.append(matrix[top][i])
            top += 1 #shifting top by 1
            #get every i in the right column
            for i in range(top,bottom):
                res.append(matrix[i][r -1 ]) #becuase right is out of bound
            r -= 1
            
            if not (l < r and top < bottom):
                break
            #get every i in the bottom row
            for i in range(r -1, l-1, -1):
                #do in reverse order from right to left
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            #get every i in the left col
            for i in range(bottom -1, top - 1, -1):
                res.append(matrix[i][l])
            l += 1
            
        return res
