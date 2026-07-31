import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # intervals problem 
        # dp[i] = max profit from 0 to i
        # sort intervals
        # at each i, either choose or not, if not, go to i+1, if yes, go to j (end)

        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}


        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
            # dont include
            res = dfs(i + 1)
            
            # bisect_right to get the first j index that is non overalpping
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))


            # include
            cache[i] = res = max(res, intervals[i][2] + dfs(j))

            return res
    
        return dfs(0)