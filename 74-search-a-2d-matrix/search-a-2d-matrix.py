class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])

        row, col = 0, C - 1  #start from the top right corner
 
        while row < R and col >= 0:
            curr = matrix[row][col]
            if curr == target:
                return True
            if curr < target:
                row += 1
            else:
                col -= 1
        
        return False


        