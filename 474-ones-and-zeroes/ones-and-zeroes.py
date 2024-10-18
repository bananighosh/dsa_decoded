class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def dfs(i, m, n):

            if i == len(strs):
                return 0
            t = strs[i].count("0")
            k = strs[i].count("1")
            pick = 0
            if m >= t and n >= k:
                pick = 1 + dfs(i+1, m-t, n-k)
            npick = dfs(i+1, m, n)
            return max(pick, npick)
        return dfs(0, m,n)
        