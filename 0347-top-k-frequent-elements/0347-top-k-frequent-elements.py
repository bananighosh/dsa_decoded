class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        freq = Counter(nums)

        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))
        
        while len(res) < k:
            count, num = heapq.heappop(heap)
            res.append(num)
        
        return res


            