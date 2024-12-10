class Solution:
    def maximumLength(self, s: str) -> int:
        subarrays = []

        for i in range(len(s)):
            index = i
            while index < len(s) and s[index] == s[i]:
                subarrays.append(s[i:index+1])
                index += 1
            
        freq_map = Counter(subarrays)
        max_len = 0

        for key,value in freq_map.items():
            if value >= 3:
                max_len = max(max_len, len(key))
        
        if max_len == 0:
            return -1
        
        return max_len
        