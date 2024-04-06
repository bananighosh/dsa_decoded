class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0

        for c in s:
            if c == '(':
                res.append(c)
                count += 1
            elif c == ')' and count > 0:
                res.append(c)
                count -= 1
            elif c != ')':
                res.append(c)
        
        final = []
        for c in res[::-1]:
            if c == '(' and count > 0:
                count -= 1
            else:
                final.append(c)
        
        return final[::-1]
        