class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #continually getting the top 2 numbers from stones

        # add stones to a max heap (by negating stones and using heapq)

        # get top 2 by popping

        # smash them together (newStone = abs(x - y)) and if newStone = 0 then dont add

        # time complexity is O(n) because at worst case there are no equals until the end and we loop through
        # space is O(n) we add all of stones to a max heap

        h = [-s for s in stones] #O(n) time to loop through entire list and negate
        heapq.heapify(h) 
        
        while len(h) > 1:
            x = heapq.heappop(h) #-4
            y = heapq.heappop(h) #-3
            newStone = x - y
            if newStone < 0:
                heapq.heappush(h, newStone)
        h.append(0) #edge case where there are no stones left
        return abs(h[0])


