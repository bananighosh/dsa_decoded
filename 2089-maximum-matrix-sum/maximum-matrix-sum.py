class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        minAbs = float("inf")
        neg = 0

        for r in matrix:
            for val in r:
                res += abs(val)

                if val < 0:
                    neg += 1
                minAbs = min(minAbs, abs(val))
        
        if neg % 2 == 0:
            return res
        else:
            return res - 2 * minAbs
                
        