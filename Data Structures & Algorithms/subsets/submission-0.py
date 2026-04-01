class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # perform a depth first search on each value 

        # select a value, call dfs iteratively on the remaining values

        # at each step of dfs, add to res, return 

        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision to NOT include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

