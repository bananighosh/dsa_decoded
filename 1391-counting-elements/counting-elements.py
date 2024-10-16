class Solution:
    def countElements(self, arr: List[int]) -> int:
        elementsSet = set(arr)
        count = 0

        for n in arr:
            if n+1 in elementsSet:
                count += 1
        
        return count

        