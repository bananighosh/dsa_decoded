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

        if not root:
            return []
        
        res = defaultdict(deque)
        dq = deque([root])
        level = 0

        while dq:
            l_size = len(dq)
            for n in range(l_size):
                node = dq.popleft()
                res[level].append(node.val)

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
            level += 1
        
        return [list(v) for v in res.values()]

        