class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        # backtrack and keep checking the lowest sum whenever adding one element in the dfs traversal ??

        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])

        # def min_path_sum(row, col):
        #     # Base case: we are in the last row
        #     if row == rows - 1:
        #         return matrix[row][col]

        #     # Recursive cases
        #     left = min_path_sum(row + 1, max(0, col - 1))
        #     center = min_path_sum(row + 1, col)
        #     right = min_path_sum(row + 1, min(cols - 1, col + 1))

        #     # Return the minimum path sum for the current position
        #     return matrix[row][col] + min(left, center, right)

        # # Iterate through the first row to find the minimum falling path sum
        # min_sum = float('inf')
        # for j in range(cols):
        #     min_sum = min(min_sum, min_path_sum(0, j))

        # return min_sum

        # Create a copy of the matrix to store the minimum falling path sum
        dp = [[0] * cols for _ in range(rows)]
        dp[0] = matrix[0]  # The first row is the same as the input matrix

        # Iterate through the matrix starting from the second row
        for i in range(1, rows):
            for j in range(cols):
                # Calculate the minimum falling path sum for the current position
                dp[i][j] = matrix[i][j] + min(dp[i-1][max(0, j-1):min(cols, j+2)])

        # The answer is the minimum falling path sum in the last row
        return min(dp[-1])

        