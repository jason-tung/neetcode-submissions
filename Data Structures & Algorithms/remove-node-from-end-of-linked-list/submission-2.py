# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = dummy = ListNode(next=head)
        r = head
        while n:
            n -= 1
            r = r.next
        while r:
            r = r.next
            l = l.next
        l.next = l.next.next
        return dummy.next