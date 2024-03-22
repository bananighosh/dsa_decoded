# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Sol 3        
        dia = [0]
        
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            dia[0] = max(dia[0], left + right)

            return 1 + max(left, right)
        
        dfs(root)

        return dia[0]

        # Sol 2
        # if not root:
        #     return 0

        # # find the height of a binary tree
        # def height(root):
        #     if not root:
        #         return 0
            
        #     l_height = height(root.left)
        #     r_height = height(root.right)

        #     return 1 + max(l_height, r_height)
        
        # left_height = height(root.left)
        # right_height = height(root.right)

        # left_dia = self.diameterOfBinaryTree(root.left)
        # right_dia = self.diameterOfBinaryTree(root.right)

        # return max((left_height + right_height), max(left_dia, right_dia))

        # # Sol 1
        # if not root:
        #     return 0

        # dia = [0] # using it as global variable

        # def dfs(root):
        #     if not root:
        #         return -1
            
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     dia[0] = max(dia[0], left + right + 2)

        #     return 1 + max(left, right)
        
        # dfs(root)
        # return dia[0]
