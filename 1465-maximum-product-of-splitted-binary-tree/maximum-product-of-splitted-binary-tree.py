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
        subTreeSums = []
        
        def sumOfTree(root):
            if not root:
                return 0
            
            left_sum = sumOfTree(root.left)
            right_sum = sumOfTree(root.right)

            currSum = root.val + left_sum + right_sum
            subTreeSums.append(currSum)

            return currSum
        
        totalSum = sumOfTree(root)

        for s in subTreeSums:
            maxProd = max(maxProd, s * (totalSum - s))
        
        return maxProd % MOD
