class Solution:
    def makeGood(self, s: str) -> str:

        # Sol 2: stack:
        stack= []

        for c in s:
            if stack and abs(ord(stack[-1]) - ord(c)) == 32:
                stack.pop()
            else:
                stack.append(c)
        
        return ''.join(stack)

        # # Sol 1: O(n) O(1)
        # left = 0
        # char_arr = list(s)

        # for right in range(len(s)):

        #     if left > 0 and abs(ord(char_arr[right]) -  ord(char_arr[left - 1])) == 32:
        #         left -= 1
        #     else:
        #         char_arr[left] = char_arr[right]
        #         left += 1
        
        # return ''.join(char_arr[:left])
                
                
        