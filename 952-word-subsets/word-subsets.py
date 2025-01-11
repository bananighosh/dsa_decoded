class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        w2_freq = Counter()
        
        for w in words2:
            for ch,cnt in Counter(w).items():
                w2_freq[ch] = max(w2_freq[ch], cnt)

        return [s for s in words1 if Counter(s)>=w2_freq]