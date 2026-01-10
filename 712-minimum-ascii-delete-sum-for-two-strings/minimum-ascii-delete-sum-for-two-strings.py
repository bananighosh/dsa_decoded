class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        n = len(s1)
        m = len(s2)

        dp = [[-1] * m for _ in range(n)]

        def solve(i , j):

            if i == n and j == m:
                return 0
            
            if i == n:
                return ord(s2[j]) + solve(i , j + 1)
            
            if j == m:
                return ord(s1[i]) + solve(i + 1, j)
            
            if dp[i][j] != -1:
                return dp[i][j]

            if(s1[i] == s2[j]):
                dp[i][j] = solve(i + 1,  j + 1)
            else:
                del_s1_i = ord(s1[i]) + solve(i + 1, j)
                del_s2_j = ord(s2[j]) + solve(i, j + 1)
                dp[i][j] = min(del_s1_i, del_s2_j)

            return dp[i][j]
        
        return solve(0, 0)
