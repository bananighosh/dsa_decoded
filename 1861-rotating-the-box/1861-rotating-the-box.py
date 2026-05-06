class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box[0]), len(box)
        res = [["" for _ in range(cols)] for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                res[r][c] = box[c][r]
            
        for r in range(rows):
            res[r].reverse()
        
        for c in range(cols):
            lowest_row_with_empty_cell = rows - 1

            for r in range(rows - 1, -1, -1):
                if res[r][c] == "#":
                    res[r][c] = "."
                    res[lowest_row_with_empty_cell][c] = "#"
                    lowest_row_with_empty_cell -= 1
                
                if res[r][c] == "*":
                    lowest_row_with_empty_cell = r - 1
        
        return res



        