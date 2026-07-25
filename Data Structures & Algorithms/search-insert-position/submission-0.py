class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # insert if l and r are equal and we still havent found it

        l, r = 0, len(nums) - 1

        while l <= r:
            # binary search
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return l 