class Solution:
    def confusingNumber(self, n: int) -> bool:

        rotating_numbers_map = {0:0, 1:1, 6:9, 8:8, 9:6}

        num = list(str(n))
        num2 = num[::-1]
        for i, n in enumerate(num2):
            if int(n) not in rotating_numbers_map:
                return False
            num2[i] = str(rotating_numbers_map[int(n)])

        print(num2, num)
        return num2 != num







        