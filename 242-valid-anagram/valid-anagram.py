class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq_map = defaultdict(int)

        for c in s:
            freq_map[c] += 1
        
        for c in t:
            freq_map[c] -= 1
        
        for val in freq_map.values():
            if val != 0:
                return False
            

        return True
        