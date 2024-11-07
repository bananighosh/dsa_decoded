class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []

        def dfs(i, arr):
            if sum(arr) > target:
                return 
            if i == len(candidates) and sum(arr) == target:
                ans.append(arr)
                return
            if i == len(candidates):
                return
            pick = dfs(i, arr + [candidates[i]])

            npick = dfs(i+1, arr)

            return
        dfs(0, [])

        return ans


        