class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left , right = 1, max(piles)
        # res = float('inf')
        res = max(piles)

        while left <= right:
            k = ( left + right ) // 2
            hours = 0
            for pile in piles:
                # time taken to finish the pile at rate k
                hours += math.ceil(pile / k)
                # if pile % k == 0:
                #     hours += pile / k
                # else:
                #     hours += (pile // k) + 1

            if hours <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1
        
        return res
                
        