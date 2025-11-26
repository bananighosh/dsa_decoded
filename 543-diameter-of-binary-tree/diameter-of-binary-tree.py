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
        dia = [0]

        def height(root):
            if not root:
                return 0
            
            lh = height(root.left)
            rh = height(root.right)

            dia[0] = max(dia[0], lh + rh)

            return 1 + max(lh, rh)
        
        height(root)
        return dia[0]
