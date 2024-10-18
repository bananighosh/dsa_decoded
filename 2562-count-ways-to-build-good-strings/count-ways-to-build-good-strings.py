class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        @cache
        def dfs(i):
            if i > high :
                return 0
            
            if i + zero in range(low, high + 1):
                z = 1 + dfs(i+zero)
            else:
                z = dfs(i+zero)
            if i + one in range(low, high+1):
                o = 1 + dfs(i+one)
            else:
                o = dfs(i+one)
            return (z + o) % mod
        return dfs(0) % mod
        