class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        left = 0
        maxLen = 0
        hmap = {}

        for right, c in enumerate(s):
            if c not in hmap:
                hmap[c] = 0
            
            while len(hmap) > 2:
                hmap[s[left]] -= 1
                if hmap[s[left]] == 0:
                    del hmap[s[left]]
                left += 1
            
            hmap[c] += 1
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen

        