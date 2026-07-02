class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        freq = Counter(s)
        n = len(s)

        # a:2, b:1
        for c, count in freq.items():
            heapq.heappush(heap, (-count, c))

        res = [""] * n
        idx = 0

        while heap:
            count, c = heapq.heappop(heap)
            count = -count

            if count > (n + 1) // 2:
                return ""

            while count > 0:
                if idx >= n:
                    idx = 1
                res[idx] = c
                idx += 2
                count -= 1
        
        return "".join(res)


        