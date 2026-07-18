class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        low, high = 0, len(numbers) - 1
        res = []

        while low <= high:
            currSum = numbers[low] + numbers[high]

            if currSum == target:
                return [low + 1, high + 1]

                # while low < high and numbers[low] == numbers[low - 1]:
                #     low += 1
                
                # while low < high and numbers[high] == numbers[high - 1]:
                #     high -= 1
            
            elif currSum < target:
                low += 1
            else:
                high -= 1
        
        return []
            
                


        