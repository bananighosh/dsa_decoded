# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # if level % 2 == 1, add to stack and pop to print
        # of level % 2 == 0, print
        if not root:
            return []
        
        level = 0
        res = defaultdict(deque)

        dq = deque([root])

        while dq:
            l_size = len(dq)
            for i in range(l_size):
                node = dq.popleft()

                if( level % 2 == 0):
                    res[level].append(node.val)
                else:
                    res[level].appendleft(node.val)
                
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
            level += 1
        # return res.values()
        return [list(v) for v in res.values()]

        