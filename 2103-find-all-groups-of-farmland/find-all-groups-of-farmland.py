class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        row, col = len(land), len(land[0])
        vis = set()
        def dfs(i,j):
            if i not in range(row) or j not in range(col) or land[i][j] == 0 or (i,j) in vis:
                return
            self.ans[0] = max(self.ans[0], i)
            self.ans[1] = max(self.ans[1], j)
            vis.add((i,j))
            dfs(i+1, j)
            dfs(i, j+1)
        ans = []
        for i in range(row):
            for j in range(col):
                if land[i][j] == 1 and (i,j) not in vis:
                    ansup = [i,j]
                    self.ans = [i,j]
                    dfs(i,j)
                    ansup.extend(self.ans)
                    ans.append(ansup)
        return ans
