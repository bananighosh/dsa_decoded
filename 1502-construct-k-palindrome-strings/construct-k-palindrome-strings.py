class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        freq_map = Counter(s)
        count = 0

        for c, cnt in freq_map.items():
            if cnt % 2 == 1:
                count += 1
        

        return count <= k and k<= len(s)

        