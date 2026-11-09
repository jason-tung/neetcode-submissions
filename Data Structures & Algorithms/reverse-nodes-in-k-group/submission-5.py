# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = group_prev = ListNode(next=head)
        cur = head
        while cur:
            kth = group_head = cur
            for _ in range(k-1):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_prev.next, prev, group_prev = kth, kth.next, group_head
            for _ in range(k):
                nxt, cur.next, prev = cur.next, prev, cur
                cur = nxt
        return dummy.next
