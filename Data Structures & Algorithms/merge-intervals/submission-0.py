class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # brute force would be to check every interval against every interval
        # sort by first interval
        # adjacent intervals, merge if you can

        # O(nlogn)
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        # O(n)
        for start, end in intervals[1:]:
            # get the most recently added (output[-1]) interval
            lastEnd = output[-1][1]


            if start <= lastEnd: # if overlapping
                output[-1][1] = max(lastEnd, end)
            else:
                # add the unedited interval to the output if not overlapping
                output.append([start, end])
            
        return output
