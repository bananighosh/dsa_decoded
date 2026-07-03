class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        heap = []
        res = []

        for word, count in freq.items():
            heapq.heappush(heap, (-count, word))
        
        while len(res) < k:
            count, word = heapq.heappop(heap)
            res.append(word)
        
        return res

        