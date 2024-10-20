class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st1 = []
        exp = []
        
        for val in expression:
            if val == "!" or val =="|" or val == "&":
                st1.append(val)
            elif val == "t":
                exp.append(True)
                ans = True
            elif val == "f":
                exp.append(False)
                ans = False
            elif val == "(":
                exp.append("(")
            elif val == ")":
                op = st1.pop()
                while exp and exp[-1] != "(":
                    val = exp.pop()
                    if op == "!":
                        ans = not val
                    elif op == "&":
                        ans = ans and val
                    else:
                        ans = ans or val
                exp.pop()
                exp.append(ans)
        return ans


        