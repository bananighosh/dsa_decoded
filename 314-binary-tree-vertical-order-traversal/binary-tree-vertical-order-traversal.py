# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        h_map = defaultdict(list)
        dq = deque([(root,0)])

        while dq:
            node, col = dq.popleft()

            if node:
                h_map[col].append(node.val)
                print(h_map)

                dq.append((node.left, col - 1))
                dq.append((node.right, col + 1))

        return [h_map[k] for k in sorted(h_map.keys())]