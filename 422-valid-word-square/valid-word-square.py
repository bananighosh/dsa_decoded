class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        for i in range(len(words)):
            for j in range(len(words[i])):
                #if word[j][i] does not exist
                if not (j < len(words)) or not (i < len(words[j])):
                    return False
                
                if words[i][j] != words[j][i]:
                    return False
            
        
        return True
        