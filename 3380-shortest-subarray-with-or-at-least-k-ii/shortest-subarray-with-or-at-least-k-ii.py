class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_length = float("inf")
        left = right = 0
        bit_counts = [0] * 32

        def update_bit_counts(bit_counts, number, delta):
            for pos in range(32):
                if number & (1 << pos):
                    bit_counts[pos] += delta
        
        def convert_bits_to_num(bit_counts):
            res = 0
            for pos in range(32):
                if bit_counts[pos]:
                    res |= 1 << pos        
            return res
    
        while right < len(nums):
            update_bit_counts(bit_counts, nums[right], 1)

            while left <= right and convert_bits_to_num(bit_counts) >= k:
                min_length = min(min_length, right - left + 1)
                update_bit_counts(bit_counts, nums[left], -1)
                left += 1
            
            right += 1
        
        return -1 if min_length == float("inf") else min_length
