# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Sol 2:
        small = min(p.val, q.val)
        large = max (p.val, q.val)

        while root:
            # if minimum of both is greater than the current value then move to right
            if root.val < small:
                root = root.right
            # if max of both is greater than the current value then move to right
            elif root.val > large:
                root = root.left
            else:
                return root
        return None
        
        # Sol 1:
        # curr = root

        # while curr:
        #     if p.val < curr.val and q.val < curr.val:
        #         curr = curr.left
        #     elif p.val > curr.val and q.val > curr.val:
        #         curr = curr.right
        #     else:
        #         return curr
        