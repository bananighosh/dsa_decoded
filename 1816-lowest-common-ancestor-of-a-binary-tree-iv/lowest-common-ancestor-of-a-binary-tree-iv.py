# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        self.hashMap = set([node.val for node in nodes])
        def dfs(node):
            if not node or node.val in self.hashMap:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if not left:
                return right
            if not right:
                return left
            if right and left:
                return node
        return dfs(root)
        