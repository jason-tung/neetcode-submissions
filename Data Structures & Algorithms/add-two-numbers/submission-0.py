# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        co = 0
        head = dummy = ListNode()
        while l1 or l2 or co:
            n1,n2 = l1.val if l1 else 0, l2.val if l2 else 0
            raw_sum = n1 + n2 + co
            co = raw_sum // 10
            head.next = ListNode(raw_sum % 10)
            head = head.next
            l1,l2 = l1.next if l1 else None, l2.next if l2 else None
        return dummy.next