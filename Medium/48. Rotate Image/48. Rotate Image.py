class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        Reasoning
        - O(n^2) look at each cell once
        - left and right bounderies starting from the top left to the top right
        - n-1 rotation
        """
        #l:left
        ##r: right
        l,r = 0, len(matrix) -1
        
        while l < r:
            for i in range(r-l):
                top, bottom = l,r
               #becuase it is a square matric
                #save the top left
                topleft = matrix[top][l+i]
                #move bottom left into top left
                matrix[top][l+i] = matrix[bottom-i][l]
                #this shift up by one 
                
                #move bottom right into bottom left
                #it is a reverse order
                matrix[bottom - i][l] = matrix[bottom][r - i]
                #shift to the left
                
                #move top right into bottom right
                matrix[bottom][r-i] = matrix[top+i][r]
                
                #move top left into top right
                matrix[top+i][r] = topleft
                
            r -= 1
            l += 1
            
