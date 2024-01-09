# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.preOrderTraversal(root, low, high)
    

    def preOrderTraversal(self, node, low, high):
        if not node:
            return 0

        curr_val = 0
        if low <= node.val and node.val <= high:
            curr_val = node.val

        left_sum = self.preOrderTraversal(node.left, low, high)
        right_sum = self.preOrderTraversal(node.right, low, high)

        return left_sum + curr_val + right_sum 
        