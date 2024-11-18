class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        prev = next = 0
        res = [0] * len(code)

        if k == 0:
            return res
        elif k < 0:
            for i in range(len(code)):  
                
                for j in range(i-1, i+k-1, -1):
            
                    res[i] += code[j]
        else:
            for i in range(len(code)):
                for j in range(i + 1, i + k + 1):
                    res[i] += code[j % len(code)]

        return res


        