# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(root, dia):
            if not root:
                return 0
            
            lh = dfs(root.left, dia)
            rh = dfs(root.right, dia)

            dia[0] = max(dia[0], lh + rh)

            return 1 + max(lh, rh)
        
        dia = [0]
        dfs(root, dia)
        return dia[0]
        