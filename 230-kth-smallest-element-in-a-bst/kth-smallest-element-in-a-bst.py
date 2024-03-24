# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Sol 1 : O(n)
        
        count = [0]
        res = [0]        

        def inorder_dfs(root, k):
            if not root or count[0] >= k:
                return
            
            inorder_dfs(root.left, k)

            count[0] += 1
            if count[0] == k:
                res[0] = root.val
                return
            
            inorder_dfs(root.right, k)
        
        inorder_dfs(root, k)
        return res[0]
            

        


        # #Sol 2: O(nlogk)
        # min_heap = []

        # def inorder_dfs(root):
        #     if not root:
        #         return

        #     inorder_dfs(root.left)
        #     heapq.heappush(min_heap, root.val)
        #     inorder_dfs(root.right)
        
        # inorder_dfs(root)
        # return min_heap[k-1]
            


        