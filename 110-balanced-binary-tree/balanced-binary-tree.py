# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]
        
            l_height = dfs(root.left)
            r_height = dfs(root.right)

            # if the left subtree and right subtrees are balanced
            balanced = l_height[0] and r_height[0] and abs(l_height[1] - r_height[1]) <= 1
            return [balanced, 1 + max(l_height[1], r_height[1])]
        
        return dfs(root)[0]