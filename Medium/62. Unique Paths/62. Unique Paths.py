class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        Reasoning
        - we can move right or diagonal
        - recursive problem
        - cache[row][col] if we reach the spot multiple time we store it and never spot it again. <the cache gonna tell us how much squqare we need to go through to reach the destination
        - final destination gonna be 1 in order to sum the right and the down actions
        
        '''
        row = [1]*n #bottom row
        for i in range(m-1):
            newRow = [1]*n #above the bottom roq
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j+1]+row[j]
            row = newRow
        return row[0]
