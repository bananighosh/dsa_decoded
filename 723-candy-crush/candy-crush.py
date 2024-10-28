class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])

        # def find():
        #     crushed_set = set()
        #     for r in range(1, m - 1):
        #         for c in range(n):
        #             if board[r][c] == 0:
        #                 continue
        #             if board[r][c] == board[r+1][c] == board[r-1][c]:
        #                 crushed_set.add((r , c))
        #                 crushed_set.add((r + 1, c))
        #                 crushed_set.add((r - 1, c))

        #     for r in range(m):
        #         for c in range(1, n - 1 ):
        #             if board[r][c] == 0:
        #                 continue
        #             if board[r][c] == board[r][c + 1] == board[r][c - 1]:
        #                 crushed_set.add((r , c))
        #                 crushed_set.add((r, c + 1))
        #                 crushed_set.add((r, c - 1))
        #     return crushed_set
            
        # def crush(crushed_set):
        #     for (r,c) in crushed_set:
        #         board[r][c] = 0
        
        def find_and_crush():
            complete = True

            for r in range(1, m - 1):
                for c in range(n):
                    if board[r][c] == 0:
                        continue
                    if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r-1][c]):
                        board[r][c] = -abs(board[r][c])
                        board[r + 1][c] = -abs(board[r + 1][c])
                        board[r - 1][c] = -abs(board[r - 1][c])
                        complete = False

            for r in range(m):
                for c in range(1, n - 1 ):
                    if board[r][c] == 0:
                        continue
                    if abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c - 1]):
                        board[r][c] = -abs(board[r][c])
                        board[r][c + 1] = -abs(board[r][c + 1])
                        board[r][c - 1] = -abs(board[r][c - 1])
                        complete = False
            
            for r in range(m):
                for c in range(n):
                    if board[r][c] < 0:
                        board[r][c] = 0

            return complete
            
        # def crush(crushed_set):
        #     for (r,c) in crushed_set:
        #         board[r][c] = 0
        def drop():
            for c in range(n):
                lowest_zero = -1
            
                for r in range(m-1, -1, -1):
                    if board[r][c] == 0:
                        lowest_zero = max(lowest_zero, r)
                    elif lowest_zero >= 0:
                        board[r][c], board[lowest_zero][c] = board[lowest_zero][c], board[r][c]
                        lowest_zero -= 1
        
        # crushed_set = find()
        # while crushed_set:
        #     crush(crushed_set)
        #     drop()
        #     crushed_set = find()

        while not find_and_crush():
            drop()
        
        return board