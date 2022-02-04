class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        Reasoning
        - backtracking: brute force approach
        - queen can move in every direction
        - if we put queens in each row/column they are going to attack each other so it's not good
        - the positive diagonal goes from botton to the top right
        - the negative diagonal goes from top to the bottom right
        - every time we insert a queen we switch to the next row
        - keep track of positive diagonal and negative diagonal and column also with set
        - rows - cols = const, it is negative for negative diagonal
        -  rows + cols = const for positive diagonals
        - we need cols, positive diagonal and negative diagonal
        - we use decision tree
        '''
        
        col = set()
        positiveDiag = set() #r + c
        negativeDiag = set()#r - c
        
        res = []
        board = [["."]*n for i in range(n)] 
        #inizialize a board
        
        def backtracking(r):
            if r == n:
                #valid n queen solution
                copy = ["".join(row) for row in board] #join rows together
                res.append(copy)
                return
            for c in range(n):
                #allows to put queen in a position
                if c in col or (r + c) in positiveDiag or (r-c) in negativeDiag:
                    continue #skip this position
                col.add(c)
                positiveDiag.add(r+c)
                negativeDiag.add(r-c)
                board[r][c] = "Q"
                backtracking(r +1 )
                
                #now brute force
                col.remove(c)
                positiveDiag.remove(r+c)
                negativeDiag.remove(r-c)
                board[r][c] = "."
        backtracking(0)
        return res
