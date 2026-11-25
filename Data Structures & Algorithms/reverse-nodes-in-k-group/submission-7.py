# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prev_group_tail = ListNode(next=head)
        while head:
            kth = first = head
            for _ in range(k - 1):
                kth = kth.next
                if not kth:
                    return dummy.next
            prev = kth.next
            for _ in range(k):
                head.next, prev, head = prev, head, head.next
            prev_group_tail.next = kth
            # // could also be prev
            prev_group_tail = first
        return dummy.next