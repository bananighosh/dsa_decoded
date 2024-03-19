# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Sol 2: using fast and slow pointer technique
        # intuition if at any point fast and slow pointer are equal loop exists

        fast = slow = head

        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        
        return False

        # Sol1 : using hashset - O(N) O(N)
        # visited = set()
        # curr = head

        # # instead of just the value add the entire node for the list
        # while curr:
        #     if curr in visited:
        #         return True
            
        #     visited.add(curr)
        #     curr = curr.next
        
        # return False
        