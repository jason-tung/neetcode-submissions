# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prev_end = ListNode(next=head)
        while True:
            kth = prev_end
            group_start = prev_end.next
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            prev = kth.next
            cur = group_start
            for _ in range(k):
                nxt = cur.next
                cur.next=prev
                prev = cur
                cur = nxt
            # can also be kth or prev i think?
            prev_end.next = kth
            prev_end = group_start