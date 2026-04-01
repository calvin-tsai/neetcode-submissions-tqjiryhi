class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # add nums to a max heap
        # pop k - 1 times and return the kth largest

        nums = [-n for n in nums]
        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)
        
        return -(heapq.heappop(nums))