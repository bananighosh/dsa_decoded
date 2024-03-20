"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # intuition: traverse the linkedlist an store in a hasmap
        # traverse the hashmap and create the output linkedlist

        curr = head
        # if we try to reference None, we get None back
        random_map = { None: None }


        while curr:
            random_map[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            new = random_map[curr]
            new.next = random_map[curr.next]
            new.random = random_map[curr.random]
            curr = curr.next
        
        return random_map[head]
        