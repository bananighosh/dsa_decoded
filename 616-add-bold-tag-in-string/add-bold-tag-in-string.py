class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:

        res = []
        open_tag = "<b>"
        close_tag = "</b>"

        bold = [False] * len(s)

        for word in words:
            start_idx = s.find(word)
            while start_idx != -1:
                for i in range(start_idx, start_idx + len(word)):
                    bold[i] = True
                
                start_idx = s.find(word, start_idx + 1)
        
        for i in range(len(s)):
            if bold[i] and (i == 0 or not bold[i - 1]):
                res.append(open_tag)
            
            res.append(s[i])

            if bold[i] and ( i == len(s) - 1 or not bold[i + 1]):
                res.append(close_tag)
            
        
        return "".join(res)
            


        