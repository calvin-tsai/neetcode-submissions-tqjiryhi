class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        idea: able to add an opening paren any time (up to n)
        only able to add a closing paren when ()( o > c meaning there is at 
        least one more opening than closing
        use two stacks to keep track of how many we've used so far
        use backtracking (brute force) to get every combination
        """

        res = []

        def dfs(curr, numO, numC):
            if numO == 0 and numC == 0: #base case: when we used all parens
                res.append(curr)
            if numO > 0: # if we have open parens left, we can add
                dfs(curr + "(", numO - 1, numC)
            if numC > numO: # if we have used more opens than closes, we can add closing
                dfs(curr + ")", numO, numC - 1)

        dfs("", n, n)
        return res
