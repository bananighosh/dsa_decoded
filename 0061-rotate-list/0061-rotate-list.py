# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k == 0 or head == None or head.next == None:
            return head
        
        def get_len(curr):
            n = 0
            while curr.next:
                n += 1
                curr = curr.next
            return n + 1, curr
        
        n, tail = get_len(head)
        # print(n)

        k = k % n
        if k == 0:
            return head
        
        tail.next = curr = head

        for i in range(n - k - 1):
            curr = curr.next
        
        curr_head = curr.next
        curr.next = None

        return curr_head



        