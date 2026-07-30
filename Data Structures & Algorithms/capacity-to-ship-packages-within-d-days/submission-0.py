class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # brute force: start at max(weights) cap and calculate true/false each
        # binary search: [max(weights), ... , sum(weights)]
        # greedy approach to find days, add until no more and iterate

        l, r = max(weights), sum(weights)

        def isValid(cap):
            currDays = 1
            currCap = cap

            for w in weights:
                if currCap - w < 0:
                    currDays += 1
                    if currDays > days:
                        return False
                    currCap = cap

                currCap -= w
            return True
        
        res = r
        while l <= r:
            m = (l + r) // 2
            if isValid(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

