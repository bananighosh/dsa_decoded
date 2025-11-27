# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        if not root:
            return []
        dq = deque([root])
        level = 0
        res = []

        while dq:
            curr = []
            for _ in range(len(dq)):
                node = dq.popleft()

                if len(curr) == level:
                    curr.append(node.val)
                
                if node.right:
                    dq.append(node.right)
                if node.left:
                    dq.append(node.left)
            
            # res.0(curr)
            res.extend(curr)
        
        return res



        