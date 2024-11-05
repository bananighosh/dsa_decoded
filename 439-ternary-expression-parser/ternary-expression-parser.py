class Solution:
    def parseTernary(self, expression: str) -> str:

        stk = []

        i = len(expression) - 1

        while i >= 0:
            char = expression[i]

            if char in "TF0123456789":
                stk.append(char)
            elif char == '?':
                onTrue = stk.pop()
                onFalse = stk.pop()
                # if expression[i - 1] == 'T':
                #     stk.append(onTrue)
                # else:
                #     stk.append(onFalse) 
                stk.append(onTrue if expression[i-1] == 'T' else onFalse)  
                i -= 1
            
            i -= 1
        
        return stk[0]
        

        