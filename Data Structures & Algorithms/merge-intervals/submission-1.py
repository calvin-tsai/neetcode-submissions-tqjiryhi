class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start interval O(nlogn)
        # iterate, if curr start is greater than next start, merge
        # O(n)
        # merged = [currStart, max(currEnd, nextEnd)]
        # total = O(n + nlogn) = O(nlogn)

        intervals.sort(key = lambda x: x[0])

        # res list of intervals to compare against
        # most recently added can potentially be merged, no else
        res = []
        res.append(intervals[0])

        for interval in intervals[1:]:
            currStart, currEnd = res[-1]
            nextStart, nextEnd = interval

            if currEnd >= nextStart:
                # we don't know where end is, we know that next interval either consumes or is extended by curr interval
                newInterval = [currStart, max(currEnd, nextEnd)]
                res[-1] = newInterval
            else:
                res.append(interval)
        return res
        
