# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        curr = last = head

        while curr:
            curr_m = m
            curr_n = n

            while curr and curr_m != 0:
                last = curr
                curr = curr.next
                curr_m -= 1
            
            while curr and curr_n != 0:
                curr = curr.next
                curr_n -= 1
            
            last.next = curr

        return head