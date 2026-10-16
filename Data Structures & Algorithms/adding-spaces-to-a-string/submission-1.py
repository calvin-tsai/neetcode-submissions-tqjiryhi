class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        nextSpace = len(spaces) - 1
        res = [""] * (len(s) + len(spaces))
        write = len(res) - 1
        
        # T O(n)
        # S O(n)
        for i in range(len(s) - 1, -1, -1):
            res[write] = s[i]
            write -= 1

            if nextSpace >= 0 and i == spaces[nextSpace]:
                res[write] = " "
                write -= 1
                nextSpace -= 1

        return "".join(res)