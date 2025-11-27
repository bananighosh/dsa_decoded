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
            res.append(dq[-1].val)
            for _ in range(len(dq)):
                node = dq.popleft()

                #if len(curr) == 0:
                    #curr.append(node.val)
                #print(curr)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
            
        
        return res
