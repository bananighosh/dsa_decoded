# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # graph problem. 
        # find the adjacent nodes and mark them as traversed
        # at the same time increment the counter for the minutes taken

        adj_list = defaultdict(list)
        self.start_node = None

        def create_adjacency_list_dfs(root):
            if root is None:
                return
            
            if root.val == start:
                self.start_node = root
            if root.left:
                adj_list[root].append(root.left)
                adj_list[root.left].append(root)
            if root.right:
                adj_list[root].append(root.right)
                adj_list[root.right].append(root)

            create_adjacency_list_dfs(root.left)
            create_adjacency_list_dfs(root.right)
        
        create_adjacency_list_dfs(root)

        # bfs to traverse
        stk = [self.start_node]
        time = -1
        visited = set()

        while stk:
            curr_list = []
            for node in stk:
                visited.add(node)
                for adj_node in adj_list[node]:
                    if adj_node not in visited:
                        curr_list.append(adj_node)
            time += 1
            stk = curr_list
        
        return time

    #     start_node = self.find_node(root, start)

    #     visited = set()
    #     min = 0
    #     self.dfs_binary_tree(root, start_node, visited)
    #     return min

    
    # def find_node(self, node, target):
    #     if node is None: 
    #         return None
        
    #     if node.val == target:
    #         return node
        
    #     # Search in the left subtree
    #     left_search = self.find_node(node.left, target)
    #     if left_search:
    #         return left_search
        
    #     # Search in the right subtree
    #     right_search = self.find_node(node.right, target)
    #     # if right_search:
    #     return right_search
    
    # def dfs_binary_tree(self, root, node, visited):
    #     if node is not None and node.val not in visited:
    #         time = 0
    #         visited.add(node.val)
    #         self.dfs_binary_tree(node.left, visited)
    #         self.dfs_binary_tree(node.right, visited)

    #         time += 1
        
    #     return time
        