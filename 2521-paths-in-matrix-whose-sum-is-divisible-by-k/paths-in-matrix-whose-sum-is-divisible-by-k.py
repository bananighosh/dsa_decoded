class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])

        mod = 10**9 + 7

        dp = {}
        def dfs(i,j, cur):

            if (i,j,cur) in dp:
                return dp[(i,j,cur)]
            val = cur + grid[i][j]

            current = val%k
            if i == m-1 and j == n-1:
                if current == 0:
                    return 1
                else:
                    return 0

            total = 0
            if i+1 < m:
                total += dfs(i+1, j, current)
            
            if j+1 < n:
                total += dfs(i, j+1, current)

            dp[(i,j,cur)] = total % mod
            return dp[(i,j,cur)]

        return dfs(0,0,0) % mod