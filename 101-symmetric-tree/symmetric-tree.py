# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # logic: if left tree is equal to right tree

        def dfs(t1, t2):
            if not t1 and not t2:
                return True
            
            if not t1 or not t2:
                return False
            
            if t1.val != t2.val:
                return False
            
            # reason: This is like a person looking at a mirror. The reflection in the mirror has the same head, but the reflection's right arm corresponds to the actual person's left arm, and vice versa
            return dfs(t1.left, t2.right) and dfs(t1.right, t2.left)

        return dfs(root,root)
        