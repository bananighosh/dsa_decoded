class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        res = []
        # i = j = 0
        # for space in spaces:
        #     while space > 0 and i < n:
        #         res.append(s[i])
        #         space -= 1
        #         i += 1
        #     res.append(' ')

        # return ''.join(res)  
        i = 0
        for right, c in enumerate(s):
            if i < len(spaces) and right == spaces[i]:
                res.append(' ')
                i += 1
            res.append(c)

        return ''.join(res)
            

            
            

        