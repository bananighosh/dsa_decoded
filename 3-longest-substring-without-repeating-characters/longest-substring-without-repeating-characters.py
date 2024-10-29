class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()

        left= maxLen = 0

        for right, char in enumerate(s):

            while char in char_set:
                # print(char, s[left], s[right], char_set)
                char_set.remove(s[left])
                left += 1
            
            print(left, right, char_set, char)
            
            char_set.add(char)
            maxLen = max(maxLen, right - left + 1)

        return maxLen
        