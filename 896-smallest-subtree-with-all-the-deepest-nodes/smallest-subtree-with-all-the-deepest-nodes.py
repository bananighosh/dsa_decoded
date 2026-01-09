# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs_lca(node):

            if not node:
                return 0, node
            
            l_height, left_node = dfs_lca(node.left)
            r_height, right_node = dfs_lca(node.right)

            if l_height > r_height:
                return l_height + 1, left_node
            
            elif r_height > l_height:
                return r_height + 1, right_node
            
            else:
                return l_height + 1, node
        
        return dfs_lca(root)[1]