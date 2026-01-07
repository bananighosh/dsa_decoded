class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ans = []
        for num in digits[::-1]:
            carry, val = divmod(num+carry,10)
            ans.append(val)
        
        if carry:
            ans.append(carry)
        return ans[::-1]
            

        


        