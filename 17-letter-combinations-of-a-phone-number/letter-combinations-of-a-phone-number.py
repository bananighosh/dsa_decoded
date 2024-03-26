class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        digitsToChar = {1: "",
                        2: "abc",
                        3: "def",
                        4: "ghi",
                        5: "jkl",
                        6: "mno",
                        7: "pqrs",
                        8: "tuv",
                        9: "wxyz"}
        
        res = []
        curr = []
        
        def backtrack(i):
            if i >= len(digits):
                # res.append(curr.copy())
                res.append("".join(curr))
                return
            
            digit = int(digits[i])
            print(digit)

            keypad = digitsToChar[digit]

            for c in keypad:
                curr.append(c)
                backtrack(i + 1)

                curr.pop()

        backtrack(0)
        return res

