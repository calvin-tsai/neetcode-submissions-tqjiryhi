class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # brute force approach is to sort nums and iterate through
        # sort is O(nlogn) and finding min is max O(n)
        # we must go through one pass of nums - ignore negatives
        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        # [1, 2, 3, 4]
        for n in nums:
            idx = abs(n) - 1 # if we found 3, go to index 2
            if idx != -1 and idx <= len(nums) - 1:
                # set it to negative regardless of pos/neg
                if nums[idx] == 0:
                    nums[idx] = -1 * (len(nums) + 1)
                else:
                    nums[idx] = -1 * abs(nums[idx])
            
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1