class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        braces_map = {")":"(", "}":"{", "]":"["}

        for c in s:
            # if (c == '(' or c == '{' or c == '['):
            #     stk.append(c)
            # else:
            #     stk.pop()

            if c in braces_map:
                if stk and stk[-1] == braces_map[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)

        return True if not stk else False 