class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        dp = [[0] * n for _ in range(m)]

        res = 0

        for r in range(m):
            dp[r][0] = matrix[r][0]
            res += dp[r][0]
        
        print(n)
        for c in range(1, n):
            dp[0][c] = matrix[0][c]
            res += dp[0][c]
        
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 1:
                    dp[r][c] =  1 + min(dp[r-1][c], dp[r][c - 1], dp[r - 1][c - 1])
                
                res += dp[r][c]
        
        return res
