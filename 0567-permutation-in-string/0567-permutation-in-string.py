class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)

        for ch in s1:
            s1_count[ch] += 1
        
        for ch in s2[:len(s1)]:
            s2_count[ch] += 1
        
        if s1_count == s2_count:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            s2_count[s2[right]] += 1

            s2_count[s2[left]] -= 1
            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]
            
            left += 1

            if s1_count == s2_count:
                return True
        
        return False
