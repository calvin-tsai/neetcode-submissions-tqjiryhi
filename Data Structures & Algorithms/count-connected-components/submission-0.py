class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # undirected graph
        # we can use an adjacency list

        #make adjacency list 
        adj = {i : [] for i in range(n)}
        visit = [False] * n

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(i):
            visit[i] = True
            for node in adj[i]:
                if not visit[node]:
                    visit[node] = True
                    dfs(node)
    
        res = 0
        for i in range(n):
            if not visit[i]:
                res += 1
                dfs(i)
                
        return res
