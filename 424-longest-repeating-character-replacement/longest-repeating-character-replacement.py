class Solution:
    def characterReplacement(self, s: str, k: int) -> int:




        freq = defaultdict(int)
        left = 0
        maxLen = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            # Intuition behind this is  the length of the sliding window minus 
            # the most frequent element/char in the the sliding window
            # indicates the number of elements that are mismatched
            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen