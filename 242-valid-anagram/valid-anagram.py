class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hmap = {}

        for c in s:
            if c not in hmap:
                hmap[c] = 0
            
            hmap[c] += 1

        for c in t:
            if c not in hmap or hmap[c] < 0:
                return False
            else:
                hmap[c] -= 1
                
        
        for key, val in hmap.items():
            if val != 0:
                return False
        return True
        