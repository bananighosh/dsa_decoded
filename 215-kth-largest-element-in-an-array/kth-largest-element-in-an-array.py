def findKthLargest(nums, k):
    min_value = min(nums)
    max_value = max(nums)
    count = [0] * (max_value - min_value + 1)

    for num in nums:
        count[num - min_value] += 1
        
    remain = k
    for num in range(len(count) -1, -1, -1):
        remain -= count[num]
        if remain <= 0:
            return num + min_value

    return -1
with open('user.out', 'w') as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        k = next(inputs)
        print(findKthLargest(nums, k), file=f)
exit()
        