# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        t = head
        l = 0
        while t and t.next:
            l += 1
            t = t.next
        mid = head
        for _ in range(l // 2):
            mid = mid.next
        midp, mid.next, prev = mid.next, None, None
        while midp:
            nxt = midp.next
            midp.next = prev
            prev, midp = midp, nxt
        midp = prev
        h1 = head
        while h1:
            h1n = h1.next
            h1.next = midp
            h1 = midp
            midp = h1n

        
        
        