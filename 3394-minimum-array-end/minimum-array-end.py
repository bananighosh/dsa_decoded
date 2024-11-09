class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        result = 0
        binn = [0]*64
        binX = [0]*64

        for i in range(64):
            bit = (x>>i) & 1
            binX[i] = bit

            bit = (n>>i) & 1
            binn[i] = bit

        
        posX = 0
        posN = 0

        while posX < 63:

            while binX[posX] == 1 and posX < 63:
                posX += 1

            binX[posX] = binn[posN]
            posX += 1
            posN += 1
        for i in range(64):
            if binX[i] == 1:
                
                result += pow(2, i)

        return result
        



