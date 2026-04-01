class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # take the first letter and see if all strings have it
        # second letter and so on

        res = ""
        idx = 0
        while True:
            if idx < len(strs[0]):
                curr = strs[0][idx]
            else:
                return res
            for s in strs:
                if idx >= len(s) or not s[idx] == curr:
                    return res
            res += curr
            idx += 1

        