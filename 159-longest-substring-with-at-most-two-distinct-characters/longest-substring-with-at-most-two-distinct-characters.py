class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start = 0
        hashMap = {}
        ans = 0
        for i, val in enumerate(s):
            if val not in hashMap:
                hashMap[val] = 0
            hashMap[val] += 1
            while len(hashMap) > 2:
                hashMap[s[start]] -= 1
                if hashMap[s[start]] == 0:
                    del hashMap[s[start]]
                start += 1
            ans = max(ans, i-start+1)

        return ans

        