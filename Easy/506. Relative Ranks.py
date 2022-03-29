class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = collections.defaultdict(int)
        sorted_score = sorted(score, reverse=True)
        for i, val in enumerate(sorted_score):
            d[val] = i+1
        
        for i, val in enumerate(score):
            if d[val] == 1:
                score[i] = "Gold Medal"
            elif d[val] == 2:
                score[i] = "Silver Medal"
            elif d[val] == 3:
                score[i] = "Bronze Medal"
            else:
                score[i] = str(d[val])
        
        return score
