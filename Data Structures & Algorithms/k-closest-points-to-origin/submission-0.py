class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # we must compute the distance from the origin for all points (O(n) time)

        # add all distances to a min heap and pop k times to get the distances

        # convert the distance back into a point using a hashmap (in which key = point, value = distance)

        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap) #O(n) time
        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        
        return res

      