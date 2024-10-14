class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = defaultdict(int)
        for s in s1:
            s1Count[s] += 1
        s1len = len(s1)
        s2dict = defaultdict(int)
        for s in s2[:s1len]:
            s2dict[s] += 1
        for i, s in enumerate(s2[:-s1len]):
            if s2dict == s1Count:
                return True
            s2dict[s2[i+s1len]] += 1
            s2dict[s] -= 1
            if s2dict[s] == 0:
                del s2dict[s]
        return s2dict == s1Count
            
        
        