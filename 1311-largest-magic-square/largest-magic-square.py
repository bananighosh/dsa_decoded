class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        row = len(grid); col = len(grid[0])
        prefixRow = [[0] * (col + 1) for _ in range(row)]
        prefixCol = [[0] * col for _ in range(row + 1)]

        for r in range(row):
            for c in range(col):
                prefixRow[r][c + 1] = prefixRow[r][c] + grid[r][c]
                prefixCol[r + 1][c] = prefixCol[r][c] + grid[r][c]
        
        def existMagicSquare(row, col, currSize):
            targetSum = prefixRow[row][col + currSize] - prefixRow[row][col]

            for r in range(row, row + currSize):
                if prefixRow[r][col + currSize] - prefixRow[r][col] != targetSum:
                    return False
            
            for c in range(col, col + currSize):
                if prefixCol[row + currSize][c] - prefixCol[row][c] != targetSum:
                    return False
            
            d1 = d2 = 0
            for i in range(currSize):
                d1 += grid[row + i][col + i]
                d2 += grid[row + i][col + currSize - 1 - i]
            if d1 != targetSum or d2 != targetSum:
                return False
            
            return True

        maxSize = min(row, col)

        while maxSize >= 2:
            for r in range(0, row - maxSize + 1):
                for c in range(0, col - maxSize + 1):
                    if existMagicSquare(r, c, maxSize):
                        return maxSize
            
            maxSize -= 1
        return 1
        