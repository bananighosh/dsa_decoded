class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        freq = Counter(s)
        res = []

        for c, count in freq.items():
            heapq.heappush(heap, (-count, c))
        
        while heap:
            count, c = heapq.heappop(heap)
            count = -count

            for cnt in range(count):
                res.append(c)
        
        return "".join(res)
        