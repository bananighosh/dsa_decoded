class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map = defaultdict(int)

        for char in s:
            freq_map[char] += 1
        
        for char in t:
            freq_map[char] -= 1
        

        for val in freq_map.values():
            if val != 0:
                return False
        
        return True
        