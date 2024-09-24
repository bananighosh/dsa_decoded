class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        st = []
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    st.append((i,j))
        direction = [(0,1), (1,0), (-1,0), (0,-1)]
        time = 0
        while st:
            if fresh == 0:
                return time
            curr = []
            time += 1
            for i,j in st:
                for x,y in direction:
                    currx, curry = i+x, j+y
                    if currx in range(m) and curry in range(n) and grid[currx][curry] == 1:
                        curr.append((currx, curry))
                        grid[currx][curry] = 2
                        fresh -= 1
            st = curr

        return time if fresh == 0 else -1
                
                    

        