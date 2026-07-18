class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cand = {}
        for i in range(1, n + 1):
            cand[i] = 0


        for t in trust:
            ai = t[0]
            bi = t[1]
            if ai in cand:
                del cand[ai]
            if bi in cand:
                cand[bi] += 1
        
        for c, i in cand.items():
            if i == n - 1:
                return c
        return -1

