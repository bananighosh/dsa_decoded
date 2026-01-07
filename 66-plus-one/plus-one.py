class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1

        for n in digits[::-1]:
             cSum = n + carry
             carry = cSum // 10
             
             cSum = cSum % 10
             res.append(cSum)

             
        
        if carry:
            res.append(1)
        
        return res[::-1]
            
        