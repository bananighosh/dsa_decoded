class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        mini_one = float("inf")
        mini_two = float("inf")

        for n in nums:
            total += n

            if n % 3 == 1:
                mini_two = min(mini_two, n + mini_one)
                mini_one = min(mini_one, n)
            if n % 3 == 2:
                mini_one = min(mini_one, n + mini_two)
                mini_two = min(mini_two, n)
        
        if total % 3 == 0:
            return total
        if total % 3 == 1:
            return total - mini_one
        if total % 3 == 2:
            return total - mini_two

        
            
            
            
        

