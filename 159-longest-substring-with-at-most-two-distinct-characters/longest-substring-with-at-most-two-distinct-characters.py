class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if( n < 3):
            return n
        left = right = 0

        char_map = defaultdict()
        max_len = 0

        while right < n:
            char_map[s[right]] = right
            right += 1
                
            if len(char_map) == 3:
                char_to_remove_idx = min(char_map.values())
                # char_set.discard(s[char_to_remove_idx])
                del char_map[s[char_to_remove_idx]]
                left = char_to_remove_idx + 1
                # right += 1
            
            max_len = max(max_len, right - left)
        
        return max_len

        