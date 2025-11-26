# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        maxSum = [float('-inf')]

        def dfs(root):
            if not root:
                return 0
            
            leftSum = max(0, dfs(root.left))
            rightSum = max(0, dfs(root.right))

            maxSum[0] = max(maxSum[0], leftSum + rightSum + root.val)

            return max(leftSum, rightSum) + root.val
        
        dfs(root)
        return maxSum[0]
        