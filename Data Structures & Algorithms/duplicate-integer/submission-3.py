class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = set()
        # Time complexity O(n)
        for num in nums:
            if num in map:
                return True
            else:
                map.add(num)
        return False
            