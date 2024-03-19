# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ## Sol 1 : iterative
        head = ListNode()
        tail = head
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return head.next

        ## Sol2 : recursive
        # def mergeRecusive(list1, list2):
        #     if list1 and list2:
        #         if list1.val < list2.val:
        #             list1.next = mergeRecusive(list1.next, list2)
        #             return list1
        #         else:
        #             list2.next = mergeRecusive(list1, list2.next)
        #             return list2
            
        #     if list1:
        #         return list1
        #     else:
        #         return list2

        # return mergeRecursive(list1, list2)
                