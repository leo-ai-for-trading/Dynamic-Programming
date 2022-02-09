class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Reasoning
        - binary search
        
        '''
        Rows, Cols = len(matrix),len(matrix[0])
        topR, botR = 0, Rows -1
        while topR <= botR:
            row = (topR+botR) // 2
            if target > matrix[row][-1]:
                topR = row + 1
                #we wanna look at rows larger 
                
            elif target < matrix[row][0]:
                botR = row -1 #shift up
            else:
                break
        if not (topR <= botR):
            return False
        row = (topR + botR) // 2
        l,r = 0, Cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m -1 
            else:
                return True
        return False
