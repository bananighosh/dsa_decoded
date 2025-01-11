class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)

        def custom_sort(n):
            return(freq[n], -n)
        
        nums.sort(key=custom_sort)

        return nums
        