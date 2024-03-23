# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)

        while q:
            q_len = len(q)
            level = []

            for i in range(q_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                res.append(level)
        
        return res


        # Sol 1
        # res = []
        # level = 0

        # def _level(root, level):
        #     if not root:
        #         return
            
        #     if len(res) <= level:
        #         res.append([])
            
        #     res[level].append(root.val)

        #     _level(root.left, level + 1)
        #     _level(root.right, level + 1)

        # _level(root, level)
        # return res
        