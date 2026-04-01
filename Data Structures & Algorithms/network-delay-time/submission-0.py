class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # if the algorithm completes and the visited nodes length != n, return -1
        # djikstra's algorithm

        edges = defaultdict(list)

        # adjacency list - u, list of [v,w]
        for u, v, w in times:
            edges[u].append((v, w))
        
        # start with given start node. takes 0 cost cuz we started there
        minHeap = [(0, k)]
        visit = set() # visit set
        t = 0 # total time
        while minHeap:
            # pop the minimum value (first value is path or w1)
            w1, n1 = heapq.heappop(minHeap)

            #skip if n1 is already visited
            if n1 in visit:
                continue
            
            # visit n1
            visit.add(n1)
            t = max(t, w1)

            # go through all edges in n1
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, [(w1 + w2), n2])
        # time O(E * logV)
        return t if len(visit) == n else -1