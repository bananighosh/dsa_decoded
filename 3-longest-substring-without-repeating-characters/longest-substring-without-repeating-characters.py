class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = maxLen = 0
        char_set = set()
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        # maxLen = 0
        # freq = set()
        # left = right = 0

        # # while right < len(s):
        # #     if s[right] not in freq:
        # #         freq[s[right]] = right
        # #         maxLen = max(maxLen, right - left + 1)
        # #     else:
        # #         left += 1
        # #         del freq[s[left]]

        # while right < len(s):
        #     while s[right] in freq:
        #         # del freq[s[left]]
        #         freq.remove(s[left])
        #         left += 1
            
        #     freq.add(s[right])
        #     maxLen = max(maxLen, right - left + 1
        
        return maxLen
        