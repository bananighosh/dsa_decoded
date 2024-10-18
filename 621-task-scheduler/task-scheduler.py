class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [-i for i in Counter(tasks).values()]
        heapq.heapify(maxHeap)
        q = deque()

        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt, time + n))
            if q and time == q[0][1]:
                cnt, time  = q.popleft()
                heapq.heappush(maxHeap,cnt)
        return time




        

        