class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        # 2, 2, 2, 3  val = 3
        #    ^  ^
        while i < n:
            if nums[i] == val:
                n -= 1  #increment n backwards and set
                nums[i] = nums[n]
            else:
                i += 1
        return n