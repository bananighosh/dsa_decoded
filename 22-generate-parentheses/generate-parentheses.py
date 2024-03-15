class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # solve this with backtracking while generating the parenthesis

        def dfs(open, close, str):
            if len(str) == n * 2:
                res.append(str)
                return
            
            if open < n:
                dfs( open + 1, close, str + "(")
            
            if close < open:
                dfs( open, close + 1, str + ")")
            
        
        res = []

        dfs(0, 0, "")

        return res




        