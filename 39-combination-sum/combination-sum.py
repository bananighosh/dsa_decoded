class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(i, target):
            if target == 0:  #and i >= len(candidates):
                res.append(curr.copy())
                return
            
            if target < 0 or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            backtrack(i, target - candidates[i])

            curr.pop()
            backtrack(i + 1, target)
        
        backtrack(0, target)
        return res
        