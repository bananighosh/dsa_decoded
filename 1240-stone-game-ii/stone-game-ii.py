class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        dp = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(2)]

        def solveForAlice(person, i, M):

            if i >= n:
                return 0
            
            if dp[person][i][M] != -1:
                return dp[person][i][M]
            
            res = -1 if person == 1 else float("inf")

            stones = 0

            for x  in range(1, min(2*M, n - i)+ 1):

                stones += piles[i + x -1]

                if person == 1: # Alice
                    res = max(res, stones + solveForAlice(0, i + x, max(M, x) ))
                else:
                    res = min(res, solveForAlice(1, i + x, max(M, x)))
            
            dp[person][i][M] = res
            return res

        return solveForAlice(1, 0, 1) # (person, i, M)
        