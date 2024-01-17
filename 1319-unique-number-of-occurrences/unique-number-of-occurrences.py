class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # vis = [-1] * len(arr)
        # # new_set = set()
        # n = len(arr)

        # for item in arr:
        #     idx = item % n

        #     print(idx, vis)
        #     if vis[idx] != -1:
        #         return False
        #     vis[idx] = 1
        # # new_set.update(arr)

        # # print(arr, new_set, len(arr) == len(new_set))
        
        # # return len(arr) == len(new_set)
        # return True

        vis = {}

        # Count occurrences using a dictionary
        for item in arr:
            vis[item] = vis.get(item, 0) + 1

        # Check if the number of occurrences is unique
        return len(vis.values()) == len(set(vis.values()))


        