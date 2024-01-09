# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # brute force
        # traverse each trees and store the leaves in a list
        # compare the list and return

        res1 = []
        res2 = []


        res1 = self.getTreeLeaves(root1, res1)
        res2 = self.getTreeLeaves(root2, res2)

        return res1 == res2
    
    def getTreeLeaves(self, node, res):
        if not node:
            return []
        
        if node.left is None and node.right is None:
            res.append(node.val)
        
        self.getTreeLeaves(node.left, res)
        self.getTreeLeaves(node.right, res)

        return res

