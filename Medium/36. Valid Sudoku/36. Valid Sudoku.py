class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        - go through every single row to check if it has already have the number
        - this process needs an hashset for each row and find any duplicates
        - O(9^2) size of the grid
        - [1,1] rapresents the subset of the square in the centre of the grid so we are getting the coordinates 
        - key = (row/3, column/3)
        - val = hashSet-> checking if it has duplicate: 
            - False it means that the sudoku is not valide
            - True we finish 
        
        '''
        cols = collections.defaultdict(set) #hashmap where the set is gonna be the value and cols the key. 
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) #key = (r/3, c/3)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": #if it's empty
                    continue
                if (board[r][c] in rows[r] or #if we find duplicate in rows
                    board[r][c] in cols[c] or #if we find duplicate in cols
                    board[r][c] in squares[(r //3, c//3)]): # tell us which squares we are in
                    return False #sudoku is not valid
                cols[c].add(board[r][c])
                rows[c].add(board[r][c])
                squares[(r //3, c//3)].add(board[r][c])
        return True
