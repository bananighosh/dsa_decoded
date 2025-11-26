# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        # DFS
        if not root:
            return []
        
        res = []

        def dfs(root, level):

            if level == len(res):
                res.append([])
            
            res[level].append(root.val)

            if root.left:
                dfs(root.left, level + 1)
            
            if root.right:
                dfs(root.right, level + 1)

        dfs(root, 0)
        return res