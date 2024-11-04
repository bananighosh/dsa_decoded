class Solution:
    def compressedString(self, word: str) -> str:

        ans = ""

        prev = word[0]

        count = 0

        for char in word:
            if char == prev and count == 9:
                ans += str(count) + char
                count = 1
            elif char == prev:
                count += 1
            else:
                ans += str(count) + prev
                prev = char
                count = 1
        ans += str(count) + prev

        return ans
            
            

      



        