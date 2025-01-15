class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def count_bits(n):
            res = 0
            while n > 0:
                res += 1 & n
                n = n >> 1
            return res
        
        cnt1, cnt2 = count_bits(num1), count_bits(num2)
        i = 0
        x = num1

        # Remove the LSB
        while cnt1 > cnt2:
            if x & (1 << i):
                cnt1 -= 1
                x = x ^ (1 << i) # unset the bit
            i += 1

        # Adding the LSB
        while cnt1 < cnt2:
            if (x & (1 << i)) == 0:
                cnt1 += 1
                x = x | (1 << i) # set the bit
            i += 1
        
        return x
        