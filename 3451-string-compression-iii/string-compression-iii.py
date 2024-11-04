class Solution:
    def compressedString(self, word: str) -> str:

        res = []
        n = len(word)

        cnt = 1
        left = 0
        for right in range(1, n):
            if word[right] == word[left]:
                if cnt == 9:
                    res.append(str(cnt))
                    res.append(word[left])
                    cnt = 0
                cnt += 1
            else:
                res.append(str(cnt))
                res.append(word[left])
                left = right
                cnt = 1
        
        res.append(str(cnt))
        res.append(word[left])
    
        
        return "".join(res)

      



        