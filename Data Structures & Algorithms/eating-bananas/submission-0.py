class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k) # p / k rounded up is number of hours for each pile

            if hours <= h: # the rate of k is high enough, can we do better?
                r = k - 1
                res = min(res, k)
            else: # the rate of k is too low, since it takes too long
                l = k + 1
        return res