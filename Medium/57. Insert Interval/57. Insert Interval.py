class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        
        Reasoning
        - take the min and the max of the two interval and merge them together
        - iterate of the sorted interval and find the insertion point 
        - if the starter value of the interval is greater than the starter of the previous interval than they are overlapping and we need to merge by the max of the first interval and the minimum of the second interval
        - the second condition is that that the max value of the first interval must be smaller of the minimum value of the second interval
        - O(n)
        """
        
        res = []
        for i in range(len(intervals)):
            #edge cases
            if newInterval[1] < intervals[i][0]:
                #less than the start value
                res.append(newInterval)
                #the interval after are not overlapping
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                #they are not overlapping
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
        
        res.append(newInterval)
        return res
