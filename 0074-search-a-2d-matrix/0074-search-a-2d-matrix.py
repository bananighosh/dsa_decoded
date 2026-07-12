class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        R, C = len(matrix), len(matrix[0])

        row, col = 0, C - 1

        while row < R and col >= 0:
            curr = matrix[row][col]

            if curr == target:
                return True
            elif curr < target:
                row = row + 1
            else:
                col = col - 1
            
        return False
