class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #zigzag means that the order of reading is zigzag
        #the output is the reading by row
        #if numRows = 1 -> return input
        #r: rows
        #the size of the "V", it's the pattern, decrease by 2 each time
        #O(n) where n is the size of s
        res = ""
        if numRows == 1: return s
        for r in range(numRows):
            increment = 2 * (numRows - 1) #the jumpo we make
            for i in range(r,len(s),increment): #for the first and last row
                res += s[i]
                if (r > 0 and r < numRows - 1 and i + increment - 2*r < len(s)): 
                #this one is for the middle row
                    res += s[i+increment - 2 * r]
        return res
