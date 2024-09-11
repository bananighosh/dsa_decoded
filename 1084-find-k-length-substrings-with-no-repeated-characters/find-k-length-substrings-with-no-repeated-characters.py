class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        start = 0
        hashSet = set()
        ans = 0
        for i, char in enumerate(s):
            while char in hashSet:
                hashSet.remove(s[start])
                start += 1
            hashSet.add(char)
            if i - start + 1 == k:
                ans += 1
                hashSet.remove(s[start])
                start += 1
        return ans


        