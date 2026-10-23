# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        node = head
        while node:
            l += 1
            node = node.next
        node = head
        target = l - n
        if target == 0:
            return head.next
        last = None
        while node:
            if not target:
                last.next = node.next
                return head
            last = node
            node = node.next
            target -= 1
        