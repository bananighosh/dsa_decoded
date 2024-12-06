class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        # res = []
        count = 0
        sum_so_far = 0
        banned = set(banned)
        for i in range(1,n+1):
            if i not in banned:
                if sum_so_far + i <= maxSum:
                    # res.append(i)
                    count += 1
                    sum_so_far += i
                else:
                    break
        
        # return len(res)
        return count
