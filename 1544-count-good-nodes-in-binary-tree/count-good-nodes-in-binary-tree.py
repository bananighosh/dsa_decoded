# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # keep finding the max in every recursion
        # update the total num of good nodes in the path from root to currMax
        
        def dfs(root, curr_max):

            if not root:
                return 0
            
            res = 1 if root.val >= curr_max else 0
            curr_max = max(curr_max, root.val)

            res += dfs(root.left, curr_max)
            res += dfs(root.right, curr_max)

            return res

        return dfs(root, root.val)

        
        