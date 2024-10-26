class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        row, col = len(rooms), len(rooms[0])
        visited = set()

        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    queue.append(((i,j), 0))
                    visited.add((i,j))
        while queue:
            top = queue.popleft()
            x,y = top[0]
            dist = top[1]
            rooms[x][y] = dist
            direction = [(0,1), (1,0), (0,-1), (-1,0)]
            for xdir, ydir in direction:
                xnew, ynew = x + xdir, y + ydir
                if (xnew, ynew) in visited or xnew not in range(row) or ynew not in range(col) or rooms[xnew][ynew]== -1:
                    continue
                queue.append(((xnew, ynew), dist + 1))
                visited.add((xnew, ynew))
