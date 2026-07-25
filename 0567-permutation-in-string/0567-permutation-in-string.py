class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_count = defaultdict(int)
        s2_count = defaultdict(int)

        n1, n2 = len(s1), len(s2)

        for c in s1:
            s1_count[c] += 1

        for c in s2[:n1]:
            s2_count[c] += 1
        
        if s1_count == s2_count:
            return True
        
        left = 0
        for right in range(n1, n2):
            s2_count[s2[right]] += 1

            s2_count[s2[left]] -= 1
            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]   
            left += 1
    
            if s1_count == s2_count:
                return True
        
        return False
        

        