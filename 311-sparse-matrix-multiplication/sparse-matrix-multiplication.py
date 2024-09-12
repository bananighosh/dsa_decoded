class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m,n,k = len(mat1), len(mat1[0]), len(mat2[0])
        ans = [[0]*k for i in range(m)]
        for i in range(m):
            for j in range(k):
                ans1 = 0
                for t in range(n):
                    ans1 += mat1[i][t] * mat2[t][j]
                ans[i][j] = ans1
        return ans
                

        