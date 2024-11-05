class Solution:
    def findPermutation(self, s: str) -> List[int]:

        res = []
        stk = []
        curr = 1

        s += "I"

        for c in s:
            if c == "I":
                stk.append(curr)
                while stk:
                    res.append(stk.pop())
            else:
                stk.append(curr)
            
            curr += 1
        
        while stk:
            res.append(stk.pop())

        return res
        