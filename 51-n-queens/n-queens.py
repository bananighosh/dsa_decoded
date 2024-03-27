class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diag = set()
        neg_diag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(row):

            if row == n:
                curr = ["".join(row) for row in board]
                res.append(curr)
                return
            
            for c in range(n):
                if c in col or (row + c) in pos_diag or (row - c) in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(row + c)
                neg_diag.add(row - c)
                board[row][c] = "Q"

                backtrack(row + 1)

                col.remove(c)
                pos_diag.remove(row + c)
                neg_diag.remove(row - c)
                board[row][c] = "."
            
        backtrack(0)
        return res

        