class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        @cache
        def lcs(i,j):
            if i == n or j == n:
                return 0
            if s1[i] == s2[j]:
                pick = 1 + lcs(i+1, j+1)
            else:
                pick = max(lcs(i+1, j), lcs(i, j+1))
            return pick
        s1 = s
        s2 = s[::-1]

        return n - lcs(0,0)
        