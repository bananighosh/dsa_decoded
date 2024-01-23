class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # create each subsequence and if it doesn't work
        # backtrack for the next sequence
        # doesn't work => not the longest string
        
        def backTrack(arr, currStr, start, maxLenStr):
            if maxLenStr[0] < len(currStr):
                maxLenStr[0] = len(currStr)
            
            for i in range(start, len(arr)):
                if not isUnique(currStr, arr[i]):
                    continue
                
                backTrack(arr, currStr + arr[i], i + 1, maxLenStr)
            
        def isUnique(currStr, newStr):
            charSet = set()

            for ch in newStr:
                if ch in charSet:
                    return False
                
                charSet.add(ch)

                if ch in currStr:
                    return False
            
            return True
        
        maxLenStr = [0]
        backTrack(arr,  "", 0, maxLenStr)
        return maxLenStr[0]