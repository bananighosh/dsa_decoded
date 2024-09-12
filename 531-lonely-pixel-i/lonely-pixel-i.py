class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row, col = len(picture), len(picture[0])
        ans = 0
        visited = set()
        for i in range(row):

            for j in range(col):
                if picture[i][j] == "B":
                    visited.add(i)
                    visited.add(j)
                    flag = True
                    for k in range(row):
                        if picture[k][j] == "B" and k != i:
                            
                            flag = False
                            break
                    for k in range(col):        
                        if picture[i][k] == "B" and k != j:
                            flag = False
                   
                            break  
                    if flag:
                        ans += 1
        return ans                     