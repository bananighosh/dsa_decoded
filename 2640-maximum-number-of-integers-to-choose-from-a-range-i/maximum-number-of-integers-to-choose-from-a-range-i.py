class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        res = []
        sum_so_far = 0
        for i in range(1,n+1):
            if i not in banned:
                if sum_so_far + i <= maxSum:
                    res.append(i)
                    sum_so_far += i
                else:
                    break
        
        return len(res)
