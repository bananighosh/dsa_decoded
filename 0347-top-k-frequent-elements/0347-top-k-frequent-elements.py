class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        res = []
        heap = []
        freq = Counter(nums)

        for num, count in freq.items():
            heapq.heappush(heap , (-count, num))
        
        while k > len(res):
            count, num = heapq.heappop(heap)
            res.append(num)
        
        return res

        