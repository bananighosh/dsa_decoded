# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0
        def dfs(node, total):
            if not node:
                return
            self.maxi = max(self.maxi, total)
            if node.left:
                if node.left.val == node.val + 1:
                    dfs(node.left, total + 1)
                else:
                    dfs(node.left, 1)
            if node.right:
                if node.right.val == node.val +1:
                    dfs(node.right, total + 1)
                else:
                    dfs(node.right, 1)
        dfs(root, 1)
        return self.maxi
