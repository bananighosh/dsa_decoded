class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # reverse each word and then reverse the entire string
        # reverse by swapping high low ends

        def reverse(s, low, high):
            while low < high:
                temp = s[low]
                s[low] = s[high]
                s[high] = temp
                low += 1
                high -= 1
            return s
        
        s.reverse() # reverse entire string
        
        l = h = 0
        while(l < len(s)):
            while h < len(s) and s[h] != " ":
                h += 1
            
            # h = i - 1

            s = reverse(s, l, h - 1)
            l = h + 1
            h += 1  
