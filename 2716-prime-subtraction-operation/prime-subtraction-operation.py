class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def isPrime(n):
            for i in range(2, isqrt(n) + 1):
                if n % i == 0:
                    return False
            return True
        
        maxElem = max(nums)
        prev_prime = [0] * (maxElem + 1)
        
        for i in range(2, maxElem + 1):
            if isPrime(i):
                prev_prime[i] = i
            else:
                prev_prime[i] = prev_prime[i - 1]
        
        for i in range(len(nums)):
            if i == 0:
                bound = nums[0]
            else:
                bound = nums[i] - nums[i - 1]
        
            if bound <= 0:
                return False
        
            largest_prime = prev_prime[bound - 1]
            nums[i] -= largest_prime

        return True
        