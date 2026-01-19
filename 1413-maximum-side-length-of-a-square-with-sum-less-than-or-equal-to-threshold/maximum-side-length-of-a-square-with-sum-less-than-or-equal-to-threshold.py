# optimized further with prefixSum and Binary Search
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

        # binary search can be applied on the offset 
        # as we 1st try to expand the sub-matrix sum to reach threshold by increasing k
        # if it exceeds we can iterate over lower size of k
        # which is the basic logic of binary search

        def checkSquareSum(side):
            for r in range(rows - side + 1):
                for c in range(cols - side + 1):
                    r2 = r + side - 1
                    c2 = c + side - 1

                    if squareSum(r, c, r2, c2) <= threshold:
                        return True
            return False

        low, high = 1, min(rows, cols)

        while low <= high:
            mid = low + (high - low) // 2

            if checkSquareSum(mid):
                maxSide = mid
                low = mid + 1
            else:
                high = mid - 1

        return maxSide

        