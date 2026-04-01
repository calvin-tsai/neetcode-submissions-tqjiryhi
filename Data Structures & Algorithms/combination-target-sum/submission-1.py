class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # combination of integers in nums that equal target

        # select 2: option1: 2 again, option2: 5, option4: 2 + 9 > 9 so its not valid

        res = [] # only add to this when we reach target (not above or below target)
        subset = []

        # O(n^2) 
        def dfs(curr, i):
            if curr == target:
                res.append(subset.copy())
                return
            if curr > target:
                return
            # if curr < target
            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(curr + nums[j], j)
                subset.pop()
            
        dfs(0, 0)
        return res