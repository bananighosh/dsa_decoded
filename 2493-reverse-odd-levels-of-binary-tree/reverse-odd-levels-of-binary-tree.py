# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def dfs(left, right, level):
            if not left or not right:
                return

            # question states to reverse the node values
            if level % 2 == 1:
                left.val, right.val = right.val, left.val
            
            return dfs(left.left, right.right, level + 1) or \
                    dfs(left.right, right.left, level + 1)
        
        dfs(root.left, root.right, 1)
        return root
        