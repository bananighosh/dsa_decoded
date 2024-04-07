class Solution:
    def checkValidString(self, s: str) -> bool:

        #Sol 2 : instead of the chars add the indices to the stacks

        stack = []
        ast = []

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == '*':
                ast.append(i)
            else: # c == ')'
                if stack:
                    stack.pop()
                elif ast:
                    ast.pop()
                else:
                    # couldn't find an open parenthesis or 
                    # an asterisk to be treated as an open parenthesis
                    return False
        
        while stack and ast:
            if stack[-1] > ast[-1]: # if open parenthesis is not in the left of asterisk
                return False
            
            stack.pop()
            ast.pop()
        
        return not stack



        # Sol 1 : 63/83 self
        # stack = []

        # open = close = = ast = 0

        # for c in s:
        #     if c == '(':
        #         stack.append(c)
        #         open += 1
        #     elif c == ')' and stack:
        #         close += 1
        #         stack.pop()
        
        # print(f" Open : {open}")
        # print(f" close : {close}")

        # if not stack:
        #     return True
        
        # return False
        