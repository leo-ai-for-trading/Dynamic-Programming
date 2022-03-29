class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        #[t, t + duration - 1]
        #
        tot = duration
        for i in range(1,len(timeSeries)):
            #compute how much time has passed since the last attack
            diff = timeSeries[i] - timeSeries[i - 1]
            #if the difference is less than the duration of the debuff, we add the difference to the result, because the debuff gets renewad and won't tick for its full duration
            if diff <= duration:
                tot += diff
            else:
                #else branch stands for the cases when the debuff ticks for its full duration so we can add it whole after the duration the debuff expires, so it cannot be more than the duration
                tot += duration
        return tot
