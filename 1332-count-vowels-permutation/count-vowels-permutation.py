class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        hashMap = {"ab":["a","e","i","o","u"],"a":["e"], "e":["a", "i"], "i":["a","e","o","u"], "o":["i", "u"], "u":["a"]}
        @cache
        def dfs(i, last):
            if i == n:
                return 1
            curr = 0
            for val in hashMap[last]:
                curr = curr + dfs(i+1, val)
            return curr % mod
        
        return dfs(0,"ab") % mod
