class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):

            if i == len(word):
                return True
            
            if (not isSafe(r,c) or
                    board[r][c] != word[i] or
                    (r,c) in path):
                return False
            
            path.add((r,c))
            res = ( dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1) )
            
            path.remove((r,c))
            return res

        def isSafe(r, c):
            return (r in range(0, ROWS) and c in range(0, COLS))
            #     return True
            # return False


        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0): 
                    return True

        return False

        