class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones_minHeap = [-weight for weight in stones]

        heapq.heapify(stones_minHeap)

        while len(stones_minHeap) > 1:
            largest = heapq.heappop(stones_minHeap)
            second_lar = heapq.heappop(stones_minHeap)

            new_weight = abs(largest - second_lar)

            heapq.heappush(stones_minHeap, -new_weight)

        return -stones_minHeap[0]
        