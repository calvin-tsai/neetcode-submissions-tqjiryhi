class Solution:
    def rob(self, nums: List[int]) -> int:
        # brute force solution: start index 0, go through each comb
        # dp solution: look at one house, rob that one or not, build up
        
        # [rob1, rob2, n, n + 1.. ]
        # either rob1 and n or rob2 and not n
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2 
            rob2 = temp
        return rob2
