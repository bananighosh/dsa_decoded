# TBD : learn to optimize further with prefixSum and Binary Search
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows = len(mat)
        cols = len(mat[0])

        # stores sum of all elems from (0,0) to (i,j)
        prefixSum = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                up = prefixSum[r - 1][c] if r > 0 else 0
                left = prefixSum[r][c - 1] if c > 0 else 0
                diag = prefixSum[r - 1][c - 1] if r > 0 and c > 0 else 0
                prefixSum[r][c] = mat[r][c] + up + left - diag

        def squareSum(r, c , r2, c2):
            # ref notebook for this calculation and visualization
            up = prefixSum[r - 1][c2] if r > 0 else 0
            left = prefixSum[r2][c - 1] if c > 0 else 0
            diag = prefixSum[r - 1][c - 1] if r > 0 and c > 0 else 0
            currSquareSum = prefixSum[r2][c2] - up - left + diag 
            return currSquareSum
        
        maxSide = 0
        # not float('-inf') because ques expects 0 len if no such square found, ref TC

        for r in range(rows):
            for c in range(cols):
                # k is an offset to reach the diagonal end corner representing the square
                #  (i, j) to (i + offset, j + offset)
                for k in range(maxSide, min(rows - r, cols - c)): 
                    r2 = r + k
                    c2 = c + k

                    currSquareSum = squareSum(r, c, r2, c2)

                    if currSquareSum <= threshold:
                        maxSide = max(maxSide, k + 1)
                    else:
                        break
        
        return maxSide

        