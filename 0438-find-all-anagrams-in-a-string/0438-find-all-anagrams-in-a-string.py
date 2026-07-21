class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []
        
        pcount = defaultdict(int)
        window = defaultdict(int)

        for ch in p:
            pcount[ch] += 1
        
        for ch in s[:len(p)]:
            window[ch] += 1
        
        left = 0
        res = []

        if window == pcount:
            res.append(0)
        
        for right in range(len(p), len(s)):
            window[s[right]] += 1

            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

            if window == pcount:
                res.append(left)
        
        return res

        