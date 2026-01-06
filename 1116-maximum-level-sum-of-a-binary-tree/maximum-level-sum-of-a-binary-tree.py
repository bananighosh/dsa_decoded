# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        currLevelSum= []
        
        def levelOrder(root, level, currLevelSum):
            
            if not root:
                return
            
            if len(currLevelSum) == level:
                currLevelSum.append(root.val)
            else:
                currLevelSum[level] += root.val
            
            levelOrder(root.left, level + 1, currLevelSum)
            levelOrder(root.right, level + 1, currLevelSum)
        

        levelOrder(root, 0, currLevelSum)

        res = 0
        for i in range(len(currLevelSum)):
            if maxSum < currLevelSum[i]:
                maxSum = currLevelSum[i]
                res = i + 1
        
        return res

            


            


