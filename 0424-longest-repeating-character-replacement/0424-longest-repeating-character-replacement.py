class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counts = {} # char : count
        maxCount = 0 # highest freq char

        l = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            maxCount = max(maxCount, counts[s[r]])

            if r-l+1 - maxCount > k:
                counts[s[l]] -= 1
                l += 1
        
        return r-l+1