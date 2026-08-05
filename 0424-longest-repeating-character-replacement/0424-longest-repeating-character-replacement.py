class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def is_valid_substring_possible(s, substr_len, k):
            freq = {}
            max_freq = 0
            start = 0

            for end in range(len(s)):
                freq[s[end]] = freq.get(s[end], 0) + 1
                if end + 1 - start > substr_len:
                    freq[s[start]] -= 1
                    start += 1
            
                max_freq = max(max_freq, freq[s[end]])
                if substr_len - max_freq <= k:
                    return True
            return False

        lo = 1
        hi = len(s) + 1

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            if is_valid_substring_possible(s, mid, k):
                lo = mid
            else:
                hi = mid
        return lo




        