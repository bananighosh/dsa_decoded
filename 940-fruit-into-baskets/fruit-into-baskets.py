class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
    
        res = left = 0
        basket = collections.defaultdict(int)
        
        for right, tfruit in enumerate(fruits):
            basket[tfruit] += 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
        
                left += 1
        
            res = max(res, right - left + 1)
        return res
        