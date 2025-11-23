# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def dfs(node, currSum, targetSum):
            if not node:
                return False
            
            currSum += node.val
            
            if not node.left and not node.right:
                if currSum == targetSum:
                    return True
            isLeft = isRight = False
            
            if node.left:
                isLeft = dfs(node.left, currSum, targetSum)
            if node.right:
                isRight = dfs(node.right, currSum, targetSum)
            return isLeft or isRight
        
        return dfs(root, 0, targetSum)