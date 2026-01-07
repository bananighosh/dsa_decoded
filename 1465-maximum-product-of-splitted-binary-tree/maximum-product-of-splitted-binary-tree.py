# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        maxProd = float('-inf')
        
        def sumOfTree(root):
            if not root:
                return 0
            
            left_sum = sumOfTree(root.left)
            right_sum = sumOfTree(root.right)

            return root.val + left_sum + right_sum
        
        totalSum = sumOfTree(root)

        def dfs(root):
            nonlocal maxProd
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            subTreeSum = root.val + left + right
            
            maxProd = max(maxProd, (totalSum - subTreeSum) * subTreeSum)
            return subTreeSum
        
        dfs(root)
        return maxProd % MOD