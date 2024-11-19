# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        count = 0

        curr = ListNode()
        curr.next = head

        while head:
            if count < m - 1:
                count += 1
            else:
                i = 0
                while i < n and head.next:
                    head.next = head.next.next
                    i += 1
                
                count = 0
            
            head = head.next
        
        return curr.next

        