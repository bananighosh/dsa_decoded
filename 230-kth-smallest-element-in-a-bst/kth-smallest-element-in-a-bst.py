# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # traverse left of the BST for finding the lower values than the parent
        # keep decrementing k
        # once the depth is reached that's the smallest value
        # in recursion when k = 0, we have reached the kth smallest

        min_heap = []

        def inorder_dfs(root):
            if not root:
                return

            inorder_dfs(root.left)
            heapq.heappush(min_heap, root.val)
            inorder_dfs(root.right)
        
        inorder_dfs(root)
        return min_heap[k-1]
            


        