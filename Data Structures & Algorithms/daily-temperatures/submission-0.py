class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        brute force way would be to check down the list for every value in list
        O(n^2) time since at the worst case its full 0s and we iterate n + (n - 1) + (n - 2) ... times
        prefix? 
        """

        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #stack[-1][0] => first element of stack, first element of the inner list
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd) # i is current day, stackInd is day of the stack
            stack.append([t, i])
        return res
            