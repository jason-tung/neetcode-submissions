# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = prev_group_tail = ListNode(next=head)
        while head:
            la = cur_group_head = head
            for _ in range(k - 1):
                la = la.next
                if not la:
                    return res.next
            prev_group_tail.next = la
            prev = la.next
            for _ in range(k):
                nxt, head.next, prev = head.next, prev, head
                head = nxt
            prev_group_tail = cur_group_head
        return res.next
            
        