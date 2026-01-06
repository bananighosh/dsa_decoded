# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([root])
        level = 0
        maxSum  = float('-inf')
        minLevel = float('inf')

        while q:
            level += 1
            currSum = 0 

            for _ in range(len(q)):
                node = q.popleft()

                currSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if maxSum < currSum:
                maxSum = currSum
                minLevel = level
        
        return minLevel

        