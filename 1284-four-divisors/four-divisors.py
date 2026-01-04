class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        res = 0
        def findDivisors(num):
            div = set()
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    div.add(i)
                    div.add(num // i)
                    if len(div) > 4:
                        return 0
            return sum(div) if len(div) == 4 else 0
        
        for num in nums:
            res += findDivisors(num)
        return res
