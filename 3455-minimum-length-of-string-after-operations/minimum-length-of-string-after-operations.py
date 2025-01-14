class Solution:
    def minimumLength(self, s: str) -> int:
        min_len = 0

        freq = Counter(s)

        for cnt in freq.values():
            if cnt % 2 == 1:
                min_len += 1
            else:
                min_len += 2
        
        return min_len

        