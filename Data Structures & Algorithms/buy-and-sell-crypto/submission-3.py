class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            #profitable?
            if prices[l] < prices[r]:
                # check profit and see if it's the max
                # dont move l, keep it at the low price
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # we found a spot where l is less or equal to r (equal doesn't matter since we are only looking at profit)
                # 3, 4, 6, 3, 5
                l = r
            r += 1 

        return maxP