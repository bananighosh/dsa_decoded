class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        m = len(nums2)

        dp = [[float('-inf')] * m for _ in range(n) ]

        def solve(i, j):

            if i == n or j == m:
                return float('-inf')

            if dp[i][j] != float('-inf'):
                return dp[i][j]
            
            product = nums1[i] * nums2[j]
            
            include = product + solve(i + 1, j + 1)
            exc_nums1 = solve(i + 1, j)
            exc_nums2 = solve(i, j + 1)

            dp[i][j] = max(product, include, exc_nums1, exc_nums2)

            return dp[i][j]
        
        return solve(0, 0)