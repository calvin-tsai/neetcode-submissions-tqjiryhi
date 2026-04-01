class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # add everything to a hashmap - where key is the num and value is the freq
        # pop k times from sorted values() list to get the result
        # issue: we need to get the num from its corresponding value
        # solution: use a map, then convert it to a heap with tuple as its values, so popping will get us the num
        m = {}
        for n in nums: 
            m[n] = 1 + m.get(n, 0)
        
        heap = []
        heapq.heapify(heap)
        for num in m.keys():
            heapq.heappush(heap, (m[num], num))
            if len(heap) > k: 
                heapq.heappop(heap) #pop minimum since its a min heap
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

