class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # create adjacency list (O(n) time)

        N = len(edges)
        # [0, 1, 2,3,4,5] right now, all par[n] = n
        par = [i for i in range(N + 1)]
        rank = [1] * (N + 1)

        # get the parent of n
        def find(n):
            if n == par[n]:
                return par[n]
            par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2, = find(n1), find(n2)

            # if the parent of n1 and n2 are the same
            if p1 == p2:
                return False

            # now, set parents based on rank
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


