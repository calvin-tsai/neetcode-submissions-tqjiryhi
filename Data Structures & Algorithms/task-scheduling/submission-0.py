class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # since each task can be at most in one cpu cycle, we should try to do 
        # most common ones first
        
        # maxheap of char to freq
        # add most common to the list, subtract its freq, push back to maxheap
        # pop the next max element to add
        # look in last n elements of the list, if element is less than n - 1 away, put in cooldown
        # if there no elements in heap, add an "idle" 
        # push all from cooldown back to maxheap

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]

        #O(n * m) worst case if all the same 
        while maxHeap or q:
            time += 1

            if maxHeap: 
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
            