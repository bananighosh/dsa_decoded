# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # len - n - to traverse from start
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # reach to n nodes from start
        while n > 0 and right:
            right = right.next
            n -= 1

        # move both the pointers to reach to the n-1 the node
        while right:
            left = left.next
            right = right.next

        # delete the nth node
        left.next = left.next.next

        # this is the actual head of the list
        return dummy.next

        