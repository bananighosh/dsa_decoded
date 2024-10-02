# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root
        def findRight(node):
            while node.right:
                node = node.right
            return node
        def helper(node):
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            temp = node.right
            attach = findRight(node.left)
            attach.right = temp
            return node.left
        dummy = TreeNode()
        dummy.left = root
        node = root
        if node.val == key:
            dummy.left = helper(node)
            return dummy.left
        while node:
            if node.val > key:
                if node.left and node.left.val == key:
                    node.left = helper(node.left)
                node = node.left
            else:
                if node.right and node.right.val == key:
                    node.right = helper(node.right)
                node = node.right
        return dummy.left
            
        