class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by start value O(nlogn)

        intervals.sort()

        res = 0 
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]: #start from second interval
            if start >= prevEnd: #non overlap
                prevEnd = end
            else: #overlap
                res += 1
                prevEnd = min(end, prevEnd) #keep the minimum end value for optimal result
        
        return res


