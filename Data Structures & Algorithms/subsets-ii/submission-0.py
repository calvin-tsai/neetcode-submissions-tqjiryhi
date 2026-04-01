class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # we can use a set to eliminate duplicates
        # backtracking to get all possible subsets - each step, choose either
        # nothing or nums[i], and backtrack until we have all choices with combinations
        # of those choices 
        # dfs of the decision tree
        
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return
            
            # subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]: #while we are at duplicate values, skip
                i += 1
            
            backtrack(i + 1, subset)


        backtrack(0, [])
        return res



