class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        char_count = Counter(s)
        
        pq = [(-ord(c), cnt) for c, cnt in char_count.items()]
        heapify(pq)

        res = []

        while pq:
            char, count = heappop(pq)
            ch = chr(-char)
            freq = min(count, repeatLimit)
            res.append(ch * freq)

            if count > freq and pq:
                next_char , next_count = heappop(pq)
                res.append(chr(-next_char))
                if next_count > 1:
                    heappush(pq, (next_char, next_count - 1))
                heappush(pq, (char, count - freq))

        return "".join(res)        