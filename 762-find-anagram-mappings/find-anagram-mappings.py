class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {i:j for j,i in enumerate(nums2)}
        return [hashMap[i] for i in nums1]
        