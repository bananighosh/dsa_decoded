# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        res = []

        q = deque([root])

        while q:
            level = len(q)
            max_val = float("-inf")

            for _ in range(level):
                curr = q.popleft()
                max_val = max(max_val, curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            res.append(max_val)
        
        return res

