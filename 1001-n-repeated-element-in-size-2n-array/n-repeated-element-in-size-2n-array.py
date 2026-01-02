class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        store = set()
        for n in nums:
            if n in store:
                return n
            store.add(n)
        
        return -1
        