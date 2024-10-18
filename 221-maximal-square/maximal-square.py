class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        cache = {}
        self.maxi = 0
        def dfs(i,j):
            if i not in range(row) or j not in range(col):
                return 0
            if (i,j) not in cache:
                down, right,diag = dfs(i, j+1), dfs(i+1, j), dfs(i+1, j+1)
                cache[(i,j)] = 0
                if matrix[i][j] == "1":
                    cache[(i,j)] = 1 + min(down, right, diag)
            self.maxi = max(self.maxi, cache[(i,j)])
            return cache[(i,j)]
        
        
       
        dfs(0,0)

        return self.maxi**2



