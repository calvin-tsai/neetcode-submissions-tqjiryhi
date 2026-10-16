# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # since there is feedback, we can use binary search
        if n <= 0:
            return -1

        l, r = 1, n

        # T: O(logn)
        # S: O(1)
        while l <= r:
            m = (l + r) // 2
            g = guess(m)
            if g == 0:
                return m
            elif g == -1:
                r = m - 1
            elif g == 1:
                l = m + 1
        return -1