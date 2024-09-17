class Solution:


    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        visit = [[False] * n for _ in range(m)]
        def dfs(i,j):
            if visit[i][j]:
                return False
            if i == destination[0] and j == destination[1]:
                return True

            visit[i][j] = True
            direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            for x,y in direction:
                ni, nj = i,j
                while ni in range(m) and nj in range(n) and maze[ni][nj] == 0:
                    ni += x
                    nj += y
                if dfs(ni-x, nj-y):
                    return True
            return False
        return dfs(start[0], start[1])