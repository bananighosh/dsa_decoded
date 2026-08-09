class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        num = n
        while True:
            prod = 1
            curr = num
            while curr > 0:
                digit = curr % 10
                prod *= digit
                curr = curr // 10
            if prod % t == 0:
                return num
            num += 1


        