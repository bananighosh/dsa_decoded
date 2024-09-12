class Solution:
    def confusingNumber(self, n: int) -> bool:

        rotating_numbers_map = {0:0, 1:1, 6:9, 8:8, 9:6}
        t = n
        result = 0

        while n > 0:
            digit = n % 10
            if digit not in rotating_numbers_map:
                return False
            
            result = result * 10 + rotating_numbers_map[digit]

            n = n // 10

        print(t,result)
        return t != result




        