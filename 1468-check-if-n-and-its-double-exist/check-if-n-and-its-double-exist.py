class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        hashMap = set()

        for num in arr:
            if num*2 in hashMap  or (num%2==0 and num//2 in hashMap):
                return True
            hashMap.add(num)
        return False
        