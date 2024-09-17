from typing import List

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        distances = [[10**5 for _ in range(n)] for _ in range(m)]
        distances[start[0]][start[1]] = 0
        
        def dfs(i, j):
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            
            for x, y in directions:
                ni, nj = i, j
                move = 0
                
                # Move in the direction until we hit a wall or boundary
                while 0 <= ni + x < m and 0 <= nj + y < n and maze[ni + x][nj + y] == 0:
                    ni += x
                    nj += y
                    move += 1
                
                # Check if this new distance is shorter
                if distances[i][j] + move < distances[ni][nj]:
                    distances[ni][nj] = distances[i][j] + move
                    dfs(ni, nj)
        
        dfs(start[0], start[1])
        return distances[destination[0]][destination[1]] if distances[destination[0]][destination[1]] != 10**5 else -1
