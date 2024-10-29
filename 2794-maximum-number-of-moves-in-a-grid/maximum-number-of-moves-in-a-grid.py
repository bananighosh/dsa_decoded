class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        @cache
        def dfs(i,j):
            curr = grid[i][j]
            max_val = 0
            # up, forward, down = 0,0,0
            if j+1 in range(cols):
                if grid[i][j+1] > curr:
                    # forward = dfs(i, j+1)
                    max_val = max(max_val, dfs(i, j + 1))
                if i+1 in range(rows) and grid[i+1][j+1] > curr:
                        # down = dfs(i+1, j+1)
                    max_val = max(max_val, dfs(i + 1, j + 1))
                if i-1 in range(rows) and grid[i-1][j+1] > curr:
                        # up = dfs(i-1, j+1)
                    max_val = max(max_val, dfs(i - 1, j + 1))
            # return 1 + max(up, forward, down)
            return 1 + max_val

        ans = 0
        for i in range(rows):
            ans = max(ans, dfs(i,0)-1)
        return ans
            