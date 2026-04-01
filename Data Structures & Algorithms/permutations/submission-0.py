class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # select one element from nums

        # explore all possible combinations after adding nums

        # backtrack and explore a different combination

        # return the list when it reaches the lenght of nums


        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:]) # recurse all the way down to base case one by one
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0]) 
                res.append(p_copy)

        return res