class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # dp = [[0] * n for _ in range(m)]

        res = 0
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 1 and r > 0 and c > 0:
                    matrix[r][c] =  1 + min(matrix[r-1][c], matrix[r][c - 1], matrix[r - 1][c - 1])
                
                res += matrix[r][c]
        
        return res
