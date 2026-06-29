# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        r = head
        while head:
            head = head.next
            l += 1
        if n == l:
            return r.next
        head = r
        prev = None
        for i in range(l - n):
            prev = head
            head = head.next
        prev.next = head.next
        return r
        
            
        
