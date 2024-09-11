class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start, end = 0, len(s)-1
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        start = 0
        for i in range(len(s)):
            if s[i] == " ":
                front, back = start, i-1
                while front <= back:
                    s[front], s[back] = s[back], s[front]
                    front += 1
                    back -= 1
                start = i+1
        front, back = start, len(s)-1
        while front <= back:
            s[front], s[back] = s[back], s[front]
            front += 1
            back -= 1
        
        