class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using minheap we can solve this
        # insert all the array nums and the frequencies in the maxheap
        # pop top K elements
        # TC : O(nlogk)

        # counts the freq of elemensts in an array - Counter()
        # freq = Counter(nums)
        # # https://pythontic.com/algorithms/heapq/nlargest
        # return heapq.nlargest(k, freq.keys(), key = freq.get)

        # Solution 2: Bucket sort
        # sorts based on the count of the elements (max count when distinct = len(arr))
        # traverse the count arr k times from the end

        freq = Counter(nums)
        bucket = [[] for i in range(len(nums) + 1)]

        # build the bucket based on the count of each element in the array
        for num, count in freq.items():
            bucket[count].append(num)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for most_freq_list in bucket[i]:
                res.append(most_freq_list)
                if len(res) == k:
                    return res

        

        