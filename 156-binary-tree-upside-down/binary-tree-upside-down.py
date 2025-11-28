# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        curr = root
        prev = leaf = None
        while curr:
            curr.right, curr.left, curr, prev, leaf = prev, leaf, curr.left, curr, curr.right

        return prev
    
        
    
    

        
        